import psycopg2
import sys

print "Querying database for the following word list: %s" %(str(sys.argv[1:]))

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

# if no command line argument is given, print the whole db
if len(sys.argv) == 1:

    cur.execute("SELECT word, count from Tweetwordcount ORDER BY word")

    tups = cur.fetchall()

    for tup in tups:
        print str(tup)

for i in range(1, len(sys.argv)):
    
    cur.execute("SELECT word, count from Tweetwordcount WHERE word='%s'" % sys.argv[i])

    tup = cur.fetchone()

    if tup == None:
        print "%s not found in database" %(sys.argv[i])

    else:
        print "Total number of occurences of '%s': %d" %(tup[0], int(tup[1]))
