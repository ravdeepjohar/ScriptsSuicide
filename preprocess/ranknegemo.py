import sys
import simplejson
from datetime import datetime
import math
from collections import defaultdict
import re
import string
from sets import Set
from operator import itemgetter
import os




def ranknegemo (twitter_file):
    
    # open the data file
    os.chdir("../")
    tweets_json = open(twitter_file,'r')


    # initialize a counter for tweets to test
    count = 0

    setofnegative = dict()
    
    while True:
        # pre-process data
        line = tweets_json.readline().lower().strip()
        
        count += 1
        if count > 10000:
            break

        # TO run whole dataset
        if not line:
            break

        tweet = simplejson.loads(line)
        
        # read each text message
        message = tweet["doc"]["text"].encode("utf-8")
        # matches = re.findall(r'#\w*', message)
        # from_user = tweet["doc"]["from_user"]
        # from_user_id = tweet["doc"]["from_user_id"]
        negemoscore = tweet["negemo"]
        # sadscore = tweet["sad"]

        for line in setofnegative:
            setofnegative.update({negemoscore:message})





            
            print setofnegative



    for key, value in sorted(setofnegative.items(), key=itemgetter(1), reverse=True):
        negemoscore = key.split(" ")[0]
        message = key.split(" ")[1]

        print negemoscore, value

    # for s in setofhashtags:
    #     print s, setofhashtags[s]

        # print negemoscore + " " + message
        # print sadscore
        # print "*****" 


def main ():
    
    ranknegemo("nyc.trim.liwc")

         

if __name__ == "__main__":
    main()