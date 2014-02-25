import sys, string, time, pickle, re, simplejson, os, operator
from collections import defaultdict
from datetime import datetime
# from stemming.porter2 import stem
from nltk.corpus import wordnet


class tweetObject:

    def __init__(self,negemoscore,sadscore,message,username,userid,timestamp ,msg_id):
        self.negemoscore = negemoscore
        self.sadscore = sadscore
        self.message = message
        self.username = username
        self.userid = userid
        self.timestamp = timestamp
        self.msg_id = msg_id

def ranknegemo (tweetDict): 

    emofile = open("outputs/negemo.txt", 'wb')
    nooftweets = 0

    for w in sorted(tweetDict, key = lambda name: float(tweetDict[name].negemoscore), reverse=True):

        nooftweets += 1

        if(nooftweets < 5000): 

            emofile.write( tweetDict[w].username + "(" + str(tweetDict[w].userid) + ")--" + 
                tweetDict[w].message + " AT " + str(tweetDict[w].timestamp) + " With Score:" + 
                tweetDict[w].negemoscore + "\n")  

    emofile.close()

def ranksadscore (tweetDict):   

    sadfile = open("outputs/sad.txt", 'wb')
    nooftweets = 1

    sadTweets = dict()


    for w in sorted(tweetDict, key = lambda name: float(tweetDict[name].sadscore), reverse=True):

        info = [ tweetDict[w].userid, tweetDict[w].message, tweetDict[w].timestamp, tweetDict[w].msg_id ]
        sadTweets[nooftweets].append(info)
        nooftweets += 1

        if nooftweets > 10000:
            break


    pickle.dump(sadTweets, open('outputs/sad.pickle' , 'wb'))


    #     if(nooftweets < 5000): 
    #         sadfile.write( tweetDict[w].username + "(" + str(tweetDict[w].userid) + ")--" + 
    #             tweetDict[w].message + " AT " + str(tweetDict[w].timestamp) + " With Score:" + 
    #             tweetDict[w].sadscore + "\n")

    # sadfile.close()


def main ():

    tweetDictNeg = dict()
    tweetDictSad = dict()

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
        msg_id = tweet["doc"]["id"]
        #lastpart = created_at.split()[-1]
        #timestamp = time.mktime(datetime.strptime(created_at, "%a, %d %b %Y %H:%M:%S " + lastpart).timetuple()) 

        # if int(negemoscore) > 0:
        #     tweetDictNeg[count] = tweetObject(negemoscore,sadscore,message, username, userid, timestamp)

        if float(sadscore) > 0:
            tweetDictSad[count] = tweetObject(negemoscore,sadscore,message, username, userid, created_at, msg_id)

    
    #ranknegemo(tweetDictNeg)
    ranksadscore(tweetDictSad)
         

if __name__ == "__main__":
    main()