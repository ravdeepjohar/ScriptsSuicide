import sys
import simplejson
import json
from datetime import datetime
import math
from collections import defaultdict
import re
import string
from sets import Set
from operator import itemgetter
import os




def label_feature (twitter_file):
    "Labels Twitter data with features"

    # initialize a counter for inclusion terms
    
    # open the data file
  
    os.chdir("../")
    tweets_json = open(twitter_file,'r')


    # initialize a counter for tweets to test
    count = 0

    setofhashtags = dict()
    
    while True:
        # pre-process data
        line = tweets_json.readline().lower().strip()
        
        # count += 1
        # if count > 10:
        #     break

        # TO run whole dataset
        if not line:
            break

        #tweet = simplejson.loads (line)
        tweet = json.loads(line)
        
        # read each text message
        message = tweet["doc"]["text"]
        matches = re.findall(r'#\w*', message)
        from_user = tweet["doc"]["from_user"]
        from_user_id = tweet["doc"]["from_user_id"]

        m = from_user + " " + str(from_user_id)
        if m in setofhashtags:
            setofhashtags[m] += 1
        else:
            setofhashtags[m] = 1

    for key, value in sorted(setofhashtags.items(), key=itemgetter(1), reverse=True):
        username = key.split(" ")[0]
        userid = key.split(" ")[1]

        print username, '(' + userid + '):', value

    # for s in setofhashtags:
    #     print s, setofhashtags[s]


def main ():
    
    label_feature("nyc.trim.liwc")

         

if __name__ == "__main__":
    main()