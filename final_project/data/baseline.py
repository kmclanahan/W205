from countries import *
import urllib
import zipfile
import xlrd
import csv
import re
import math
import string
import psycopg2

BaselineArray=[]
for Country in Countries:
    BaselineArray.append([Country,0,0,0])

testfile = urllib.URLopener()
urllib.urlretrieve("http://databank.worldbank.org/data/download/WGI_csv.zip", "WGI_csv.zip")
zfile = zipfile.ZipFile('WGI_csv.zip')
zfile.extractall()

with open('WGI_Data.csv', 'rb') as csvfile:
    data_iter = csv.reader(csvfile, delimiter = ',', quotechar = '\"')
    data = [data for data in data_iter]

# extract data for PV indicator for African countries only
pv=[]
for row in data:
    if row[0] in Countries:
        if (row[3]=='PV.EST'):
            #print "found country", row[0], row[19]
            pv.append([row[0], row[19]])
    
    if row[0] in Misspellings:
        if (row[3]=='PV.EST'):
            idx = Misspellings.index(row[0])
            pv.append([Corrections[idx], row[19]])
            #print "found misspelling", row[0], Corrections[idx], row[19]

# correct out of range values, round up then rescale from -2.5-2.5 to 0-100
for row in range(len(pv)):
    if float(pv[row][1]) < -2.5:
        pv[row][1] = -2.5

    pv[row][1]=round((float(pv[row][1])+2.5)*20,1)

# copy the results into the result table
for arow in pv:
    for brow in BaselineArray:
        if arow[0] == brow[0]:
            brow[1]=arow[1]

###########################
# Now import the FSI data #
###########################

#open excel file
urllib.urlretrieve("http://fsi.fundforpeace.org/library/fragilestatesindex-2015.xlsx", "FSindex.xlsx")
wb = xlrd.open_workbook("FSindex.xlsx")
sh = wb.sheet_by_name('2015')

#put the country name and total column into an array
FSIndex=[]
for rownum in range(sh.nrows):
    FSIndex.append([sh.row_values(rownum)[1],sh.row_values(rownum)[2]])

            
# extract data for African countries only
ffptable = []
for rownum in range(len(FSIndex)):
    if FSIndex[rownum][0] in Countries:
        ffptable.append([FSIndex[rownum][0],FSIndex[rownum][1]])
    if FSIndex[rownum][0] in Misspellings:
        idx = Misspellings.index(FSIndex[rownum][0])
        ffptable.append([Corrections[idx], FSIndex[rownum][1]])

# rescale from 0-120 to 0-100        
for row in range(len(ffptable)):
    ffptable[row][1]=round(float(ffptable[row][1])*5/6,1)

# copy the results into the result table
for arow in ffptable:
    for brow in BaselineArray:
        if arow[0] == brow[0]:
            brow[2]=float(arow[1])

#########################################################################################################
# Calculate the average of WGI & FSI
# 
#########################################################################################################

for row in BaselineArray:
    row[3]=round((float(row[1])+float(row[2]))/2,1)

#########################################################################################################
# Monthly Crisis Group Countries
# Extract African countries mentioned in the report
# Increase baseline for countries by 5%
#########################################################################################################


printable = set(string.printable)

urllib.urlretrieve("http://feeds.feedburner.com/crisisgroup-crisiswatch", "monthlyCrisis.xml")
root = ET.parse('monthlyCrisis.xml').getroot()

monthlyCrisisGroupList=[]
num = 0
for item in root.iter('description'):
    #remove unicode characters
    text = unicode(item.text)
    text = filter(lambda x: x in printable, text)    
    
    for country in Countries:
        if country in text:
            #print "found country:", country, "in item", str(num)
            monthlyCrisisGroupList.append(country)
        
    for city in Capitals:
        if city in text:
            #print "found city:", city, "in item", str(num)
            monthlyCrisisGroupList.append(city)
    
    for misspelling in Misspellings:
        if misspelling in text:
            #print "found misspelling:", misspelling[0], "in item", str(num)
            idx = Misspellings.index(misspelling)
            monthlyCrisisGroupList.append(Corrections[idx])
            
    num += 1

for item in monthlyCrisisGroupList:
    #if it's a capital, convert to country
    if item in Capitals:
        i = monthlyCrisisGroupList.index(item)
        idx = Capitals.index(item)
        monthlyCrisisGroupList[i] = CountryCapitalPairs[idx][0]


unique_mcg_list = list(set(monthlyCrisisGroupList))

counts = [0]*len(unique_mcg_list)
for item in monthlyCrisisGroupList:
    idx = unique_mcg_list.index(item)
    counts[idx] += 1

if counts[unique_mcg_list.index("Sudan")] <= counts[unique_mcg_list.index("South Sudan")]:
    print "We didn't really find Sudan, just South Sudan, removing"
    unique_mcg_list.remove("Sudan")

#increase corresponding country baseline average by 5%
for Country in unique_mcg_list:
    for row in range(len(BaselineArray)):
        if Country == BaselineArray[row][0]:
            print ('Before', BaselineArray[row][0],BaselineArray[row][3])
            BaselineArray[row][3]=round(float(BaselineArray[row][3])*1.05,1)
            print ('After', BaselineArray[row][0],BaselineArray[row][3])

#########################################################################################################
# Bi-annual Crisis Group Countries
# Published bi-annually in December and June
# Extract African countries mentioned in the report
# Increase baseline for countries by 5%
#########################################################################################################


sock = urllib.urlopen("http://www.crisisgroup.org/en/publication-type/watch-list.aspx")
htmlSource = str(sock.read())
sock.close()

biannualCrisisGroupList=[]

#remove special characters and links
clean1 = re.sub('<[^>]*>', '', htmlSource)
clean2 = re.sub('[!@#$%^&*()[]{};:,./<>?\|`~-=_+]', ' ', clean1)
clean3 = re.sub('<?[a-zA-Z0-9_ ]+>', ' ', clean2)

# split out the chunk between the most recent and second most recent watch lists
beginhtmlbyte = clean3.split('Past Early Warning Watch Lists',1)
beginhtmlstring = str(beginhtmlbyte[1])
finalchunkbyte = beginhtmlstring.split('Watch List')
finalchunk=str(finalchunkbyte[2])

words = finalchunk.split("\n")

for word, i in zip(words, range(len(words))):
    words[i] = word.strip()

words = list(set(words))

for word in words:
    if word in Countries:
        biannualCrisisGroupList.append(word)
    
    if word in Misspellings:
        idx = Misspellings.index(word)
        biannualCrisisGroupList.append(Misspellings[idx][1])

#increase corresponding country baseline average by 5%
for Country in biannualCrisisGroupList:
    for row in range(len(BaselineArray)):
        if Country == BaselineArray[row][0]:
            print ('Before', BaselineArray[row][0],BaselineArray[row][3])
            BaselineArray[row][3]=round(float(BaselineArray[row][3])*1.05,1)
            print ('After', BaselineArray[row][0],BaselineArray[row][3])       

conn = psycopg2.connect(database="travel_info", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("TRUNCATE Baseline_Data")

for row in BaselineArray:
    cur.execute("INSERT INTO Baseline_Data (country, WGI_score, FFP_score, score) VALUES (%s, %s, %s, %s)", (row[0], row[1], row[2], row[3]))

conn.commit()
conn.close()

print "Successfully loaded WGI and FFP data in Baseline_Data table."
