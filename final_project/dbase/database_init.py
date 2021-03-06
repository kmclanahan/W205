import psycopg2


conn = psycopg2.connect(user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
cur.connection.set_isolation_level(0)

try:
    cur.execute("CREATE DATABASE travel_info")
except:
    cur.execute("DROP DATABASE travel_info")
    cur.execute("CREATE DATABASE travel_info")

conn.commit()
conn.close()

conn = psycopg2.connect(dbname="travel_info", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
cur.connection.set_isolation_level(0)
cur.execute("CREATE TABLE Twitter_Data(id serial PRIMARY KEY, tweet varchar, location varchar, country varchar, coordinates varchar, threat_type varchar)")
cur.execute("CREATE TABLE Govt_Data(id serial PRIMARY KEY, country varchar, type varchar, start_date varchar, end_date varchar, full_text varchar)")
cur.execute("CREATE TABLE Baseline_Data(id serial PRIMARY KEY, country varchar, WGI_score varchar, FFP_score varchar, score varchar)")

cur.close()

conn.commit()
conn.close()

print "created database travel_info"
print "created table Twitter_Data"
print "created table Govt_Data"
print "created table Baseline_Data"
