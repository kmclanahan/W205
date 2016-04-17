import xml.etree.ElementTree as ET
from difflib import SequenceMatcher
import re

import psycopg2

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# resolves a country name
def resolve(c):
    #remove punctuation
    c = re.sub("[,.]", "", c)
    
    # first see if any of the words in c match one of our countries
    for word in c.split():
        if word.strip() in countries:
            return countries[countries.index(word)]
    
    #next see if there's a close match
    ratios = []
    for country, i in zip(countries, range(len(countries))):
        ratios.append(similar(c, country))

    return countries[ratios.index(max(ratios))]
        
rootTW = ET.parse('TWs.xml').getroot()
rootTA = ET.parse('TAs.xml').getroot()

c_file = open("countries.txt", "r")

countries = []
for line in c_file:
    countries.append(line.strip())

conn = psycopg2.connect(database="travel_info", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("TRUNCATE Govt_Data")

# reinit the database
for item in rootTW.iter('item'):
    for child in item:
       
        if child.tag == "title":
            country = child.text[:-15]
            if "Warning" in child.text:
                ttype = "Warning"
            elif "Alert" in child.text:
                ttype = "Alert"
            else:
                ttype = "Unknown"
            
        if child.tag == "pubDate":
            startDate = child.text
        
        if child.tag == "description":
            detail = child.text

    if country not in countries:
        country = resolve(country)

    print "Adding %s for %s" %(ttype, country)

    cur.execute("INSERT INTO Govt_Data (country, type, start_date, full_text) VALUES (%s, %s, %s, %s)", (country, ttype, startDate, detail))

for item in rootTA.iter('item'):
    for child in item:
       
        if child.tag == "title":
            country = child.text[:-13]
            if "Warning" in child.text:
                ttype = "Warning"
            elif "Alert" in child.text:
                ttype = "Alert"
            else:
                ttype = "Unknown"
                
        if child.tag == "pubDate":
            startDate = child.text
        
        if child.tag == "description":
            detail = child.text
    
    start_idx = detail.find("expires on")+11
    end_idx = detail[start_idx:].find(".")
    endDate = detail[start_idx:start_idx+end_idx]
    
    print "Adding %s for %s" %(ttype, country)

    cur.execute("INSERT INTO Govt_Data (country, type, start_date, end_date, full_text) VALUES (%s, %s, %s, %s, %s)", (country, ttype, startDate, endDate, detail))

conn.commit()
conn.close()

print "Successfully loaded Travel Alerts and Warnings in Govt_Data table."
