import sys
import psycopg2


if len(sys.argv) != 2:
    print "Invalid syntax, argument must be in the form 'k1,k2' where k1 and k2 are integers"
    sys.exit()

arg = sys.argv[1].split(",")

try:
    k1 = int(arg[0])
    k2 = int(arg[1])

except:
    print "Invalid syntax, argument must be in the form 'k1,k2' where k1 and k2 are integers"
    sys.exit()

if k1 > k2:
    print "Invalid syntax, k1 must be less than k2"
    sys.exit()

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()

cur.execute("SELECT word, count from Tweetwordcount WHERE count >= %s AND count <= %s" %(k1, k2))

tups = cur.fetchall()

for tup in tups:
    print "\t%20s:%8d" %(tup)
