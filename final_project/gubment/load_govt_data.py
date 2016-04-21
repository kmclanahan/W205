import xml.etree.ElementTree as ET
from difflib import SequenceMatcher
import re
from countries import *
import psycopg2
        
rootTW = ET.parse('TWs.xml').getroot()
rootTA = ET.parse('TAs.xml').getroot()

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
                continue
            
        if child.tag == "pubDate":
            startDate = child.text
        
        if child.tag == "description":
            detail = child.text

    if country not in Countries:
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
                continue
                
        if child.tag == "pubDate":
            startDate = child.text
        
        if child.tag == "description":
            detail = child.text
    
    start_idx = detail.find("expires on")+11
    end_idx = detail[start_idx:].find(".")
    endDate = detail[start_idx:start_idx+end_idx]

    if country not in Countries:
        country = resolve(country)    

    print "Adding %s for %s" %(ttype, country)

    cur.execute("INSERT INTO Govt_Data (country, type, start_date, end_date, full_text) VALUES (%s, %s, %s, %s, %s)", (country, ttype, startDate, endDate, detail))

conn.commit()
conn.close()

print "Successfully loaded Travel Alerts and Warnings in Govt_Data table."
