import re
import simplejson


def main ():
    annotated_chris = open ("annotated_chris.json")
    annotated_cissi = open("annotated_cissi.json")
    lines_chris = annotated_chris.readlines()
    lines_cissi = annotated_cissi.readlines()

    for tag in ["HD", "LD", "H"]:
        tagit (tag,lines_chris,lines_cissi)
        
def tagit (tag,lines_chris,lines_cissi):
    json_chris = [simplejson.loads (line) for line in lines_chris]
    json_cissi = [simplejson.loads (line) for line in lines_cissi]
    user_chris = set([tweet["doc"]["from_user"] for tweet in json_chris if tweet["distress"] == tag])
    user_cissi = set([tweet["doc"]["from_user"] for tweet in json_cissi if tweet["distress"] == tag])
    id_chris = set([tweet["doc"]["id"] for tweet in json_chris if tweet["distress"] == tag])
    id_cissi = set([tweet["doc"]["id"] for tweet in json_cissi if tweet["distress"] == tag])
    
    user_both = user_chris.intersection(user_cissi)
    id_both = id_chris.intersection(id_cissi)
 
    print "Original Tweets"
    print "~~~~~~~~~~~~~~~"
    for tweet in json_cissi:
        if tweet["doc"]["id"] in id_both:
            print "%s---%s (%s):\t%s" % (tweet["distress"],tweet["doc"]["from_user"], tweet["doc"]["created_at"],tweet["doc"]["text"].encode('utf-8','ignore'))
       
        
    print "All Tweets"
    print "~~~~~~~~~~"


    all_tweets = open("data/nyc.trim.liwc")
    tweets_by_user = dict()
    while True:
        line = all_tweets.readline()
        if not line:
            break
        tweet = simplejson.loads (line)
        if tweet["doc"]["from_user"] in user_both:
            if not tweet["doc"]["from_user"] in tweets_by_user:
                tweets_by_user[tweet["doc"]["from_user"]] = list()
            tweets_by_user[tweet["doc"]["from_user"]].append(tweet)
            
    for user in tweets_by_user:
        for tweet in tweets_by_user[user]:
            print "%s (%s):\t%s" % (user, tweet["doc"]["created_at"],tweet["doc"]["text"].encode('utf-8','ignore'))

                
            
if __name__ == "__main__":
    main()

