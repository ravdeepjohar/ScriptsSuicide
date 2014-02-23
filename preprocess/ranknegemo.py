import sys, string, time, pickle, re, simplejson, os, operator
from collections import defaultdict
from datetime import datetime
# from stemming.porter2 import stem
from nltk.corpus import wordnet


class tweetObject:

    def __init__(self,negemoscore,sadscore,message,username,userid,timestamp):
        self.negemoscore = negemoscore
        self.sadscore = sadscore
        self.message = message
        self.username = username
        self.userid = userid
        self.timestamp = timestamp

def ranknegemo (tweetDict): 

    emofile = open("outputs/negemo.txt", 'wb')

    for w in sorted(tweetDict, key = lambda name: float(tweetDict[name].negemoscore), reverse=True):
         emofile.write( tweetDict[w].username + "(" + str(tweetDict[w].userid) + ")--" + 
            tweetDict[w].message + " AT " + str(tweetDict[w].timestamp) + " With Score:" + 
            tweetDict[w].negemoscore + "\n")  

    emofile.close()

def ranksadscore (tweetDict):   

    sadfile = open("outputs/sad.txt", 'wb')

    for w in sorted(tweetDict, key = lambda name: float(tweetDict[name].sadscore), reverse=True):
         sadfile.write( tweetDict[w].username + "(" + str(tweetDict[w].userid) + ")--" + 
            tweetDict[w].message + " AT " + str(tweetDict[w].timestamp) + " With Score:" + 
            tweetDict[w].sadscore + "\n")

    sadfile.close()


def main ():

    tweetDict = dict()

    os.chdir("../")
    tweets_json = open("nyc.trim.liwc",'r')
    count = 0

    while True:

        # pre-process data
        line = tweets_json.readline().lower().strip()
        
        count += 1
        # if count > 10:
        #     break

        # TO run whole dataset
        if not line:
            break

        tweet = simplejson.loads(line)
        
        # read each text message
        message = tweet["doc"]["text"].encode("utf-8")
        username = tweet["doc"]["from_user"]
        userid = tweet["doc"]["from_user_id"]
        negemoscore = tweet["negemo"]
        sadscore = tweet["sad"]
        created_at = tweet["doc"]["created_at"]
        lastpart = created_at.split()[-1]
        timestamp = time.mktime(datetime.strptime(created_at, "%a, %d %b %Y %H:%M:%S " + lastpart).timetuple()) 

        tweetDict[count] = tweetObject(negemoscore,sadscore,message, username, userid, timestamp)

    
    ranknegemo(tweetDict)
    #ranksadscore(tweetDict)
         

if __name__ == "__main__":
    main()