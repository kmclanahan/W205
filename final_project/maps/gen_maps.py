import psycopg2

html_str = """
<!DOCTYPE html>
<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['geochart']});
      google.charts.setOnLoadCallback(drawRegionsMap);

      function drawRegionsMap() {
        var data = google.visualization.arrayToDataTable([
          ['Country', 'Baseline'],
"""

conn = psycopg2.connect(database="travel_info", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("SELECT country, score FROM Baseline_Data")

all_data = cur.fetchall()

for row in all_data:
    html_str +=  "          ['%s', '%s'],\n" %(row[0], row[1])

conn.commit()
conn.close()

html_str += """
        ]);

        var options = {
          region: '002', // Africa
          colorAxis: {colors: ['#35A012','#F2E85C', '#F64809']},
          datalessRegionColor: '#D2CCC3',
          defaultColor: '#f5f5f5',
        };
        var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));
        chart.draw(data, options);
      }
    </script>
    <script type='text/javascript'>
      google.charts.load('current', {'packages': ['geochart']});
      google.charts.setOnLoadCallback(drawMarkersMap);

      function drawMarkersMap() {
        var data = google.visualization.arrayToDataTable([
          ['Country',   'Population', 'Area Percentage'],
          ['Uganda',  65700000, 50],
          ['Tanzania', 81890000, 27],
          ['Zimbabwe',  38540000, 23]
        ]);

        var options = {
          sizeAxis: { minValue: 0, maxValue: 100 },
          region: '002', // Africa
          displayMode: 'markers',
          colorAxis: {colors: ['#e7711c', '#4374e0']} // orange to blue
        };
        var chart = new google.visualization.GeoChart(document.getElementById('chart_div'));
        chart.draw(data, options);
    };
    </script>

  </head>
  <body>
    <div id="regions_div" style="width: 1400px; height: 1100px;"></div>
  </body>
</html>

"""

Html_file= open("regionChart.html","w")
Html_file.write(html_str)
Html_file.close()


# this code chunk generates the HTML file for the marker chart

html_str = """
<!DOCTYPE html>
<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type='text/javascript'>
      google.charts.load('current', {'packages': ['geochart']});
      google.charts.setOnLoadCallback(drawMarkersMap);

      function drawMarkersMap() {
        var data = google.visualization.arrayToDataTable([
          ['Country',   'Warning or Alert', 'Chatter Volume'],
"""

conn = psycopg2.connect(database="travel_info", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("SELECT country, type FROM Govt_Data")

all_data = cur.fetchall()

warnings = []
alerts = []
for row in all_data:
    if row[1] == "Warning":
        warnings.append(row[0])
    elif row[1] == "Alert":
        alerts.append(row[0])
    else:
        print "Something weird happened..."

warnings = list(set(warnings))
alerts = list(set(alerts))

for row in warnings:
    cur.execute("SELECT country FROM Twitter_Data WHERE country='%s'" % row)
    chatter = len(cur.fetchall())

    html_str +=  "          ['%s', %s, %s],\n" %(row, 1, chatter)

for row in alerts:
    if row not in warnings:
        cur.execute("SELECT country FROM Twitter_Data WHERE country='%s'" % row)
        chatter = len(cur.fetchall())

        html_str +=  "          ['%s', %s, %s],\n" %(row, 0, chatter)


conn.commit()
conn.close()

html_str += """
        ]);

        var options = {
          sizeAxis: { minValue: 0, maxValue: 100 },
          region: '002', // Africa
          displayMode: 'markers',
          colorAxis: {colors: ['#F60944', '#1B18C2']} // dark red to royal blue
        };
        var chart = new google.visualization.GeoChart(document.getElementById('chart_div'));
        chart.draw(data, options);
    };
    </script>

  </head>
  <body>
    <div id="chart_div" style="width: 1400px; height: 1100px;"></div>
  </body>
"""

Html_file= open("markerChart.html","w")
Html_file.write(html_str)
Html_file.close()

