import liwc.categories
import MySQLdb,sys
from numpy import *

def progress(perc):
  perc = int(perc)
  if perc%1 == 0:
    sys.stdout.write('\r')
    sys.stdout.write("[%-20s] %d%%" % ('='*(perc/5), perc))
    sys.stdout.flush()
  if perc == 100:
    sys.stdout.write('\n')


#### --------- MAIN ------ ####

users = open("./totalUsers.data","r")

db = MySQLdb.connect(user='root',passwd='agr4ta',db='pinterest')
c = db.cursor()

i = 0
liwcSumFemale = array((0,)*41)
liwcSumMale = array((0,)*41)
for user in users:

  q = "select description, gender from users where id = '"+user.strip() +"' and description != 'null'"
  c.execute(q)
  result = c.fetchone()
  if( result is not None ):
    description=result[0]
    gender=result[1]
    if (gender == "female"):
      tweetLiwc = array(liwc.categories.classify(description))
      liwcSumFemale += tweetLiwc
    elif ( gender == "male"):
      tweetLiwc = array(liwc.categories.classify(description))
      liwcSumMale += tweetLiwc
  i += 1
  progress(i*100/683275)
  #print description
  #print tweetLiwc
  #print liwcSum


parsFemale = liwcSumFemale.tolist()
parsMale= liwcSumMale.tolist()

for i in range(len(parsFemale)):
  if ( i >= len(parsFemale) - 2):
    break
  else:
    parsFemale[i] = float( "%.2f" % (float(parsFemale[i])/parsFemale[-2]*100))
for i in range(len(parsMale)):
  if ( i >= len(parsMale) - 2):
    break
  else:
    parsMale[i] = float( "%.2f" % (float(parsMale[i])/parsMale[-2]*100))

print "---- Female ---"
print parsFemale
print float(parsFemale[-2])/parsFemale[-1]*100
print "---- Male ---"
print parsMale
print float(parsMale[-2])/parsMale[-1]*100

