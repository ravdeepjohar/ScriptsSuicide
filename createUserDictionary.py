import sys, string, time, pickle, re, simplejson
from collections import defaultdict
from datetime import datetime


def label_feature (twitter_file):
    "Labels Twitter data with features"

    dictionaryusers = defaultdict(list)
   
    while True:
        # pre-process data
        line = tweets_json.readline().lower().strip()
        

        # comment this part to run for entire dataset
        # count += 1
        # if count > 1000:
        #     break

        # TO run whole dataset
        if not line:
            break

        tweet = simplejson.loads (line)
        
        # read each text message
        message = tweet["doc"]["text"].encode("utf-8")       
        from_user = tweet["doc"]["from_user"]
        from_user_id = tweet["doc"]["from_user_id"]
        created_at = tweet["doc"]["created_at"]
        msg_id = tweet["doc"]["id"]
        negemoscore = tweet["negemo"]
        sadscore = tweet["sad"]
        info = [message, created_at, msg_id, from_user, negemoscore, sadscore]


        # Add tweets in dictionary 
        dictionaryusers[from_user_id].append(info)

        
       
    pickle.dump(dictionaryusers, open('outputs/usertweethistory.pickle' , 'wb'))

   

def main ():

    label_feature("nyc.trim.liwc")

         

if __name__ == "__main__":
    main()
