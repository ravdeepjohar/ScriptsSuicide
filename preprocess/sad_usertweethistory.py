import re, string, os, sys, time
from datetime import datetime
from collections import defaultdict
import cPickle as pickle



def getuser_tweet_history ():

    os.chdir("../")
    dictionaryusers = pickle.load( open('outputs/usertweethistory.pickle', 'rb') )
    sadTweets = pickle.load( open('outputs/sad.pickle', 'rb') )
    globalTweet = 1     

    for tweetno in range(1,20):

        current_tweet = sadTweets[tweetno][0][1]
        current_tweet_userid = sadTweets[tweetno][0][0]
        current_tweet_date = str(sadTweets[tweetno][0][2])
        current_tweet_msg_id = sadTweets[tweetno][0][3]
        current_tweet_SadScore = sadTweets[tweetno][0][4]

        lastpart = current_tweet_date.split()[-1]
        cur_timestamp = time.mktime(datetime.strptime(current_tweet_date, "%a, %d %b %Y %H:%M:%S " + lastpart).timetuple()) 
        cur_timestamp = datetime.fromtimestamp(cur_timestamp)


        print str(globalTweet) + ": Date:" , current_tweet_date + " Msg_id:", str(current_tweet_msg_id) + " Category: Sad LIWC"
        
        userTweets = dictionaryusers[current_tweet_userid]
        sizeoflist = len(userTweets)

        location = -1

        for tweets in range(len(userTweets)):

            usrtweet= userTweets[tweets][0]
            usrtweet_msg_id = userTweets[tweets][2]

            if usrtweet_msg_id == current_tweet_msg_id:

                location = tweets
                break
                #print usrtweet

        tweetcount = 1

        if location != -1: 

            if location-5 > 0:
                for tw in userTweets[location-3:location]: 

                    tw_date = tw[1]
                    tw_lastpart = str(tw_date.split()[-1])
                    tw_timestamp = time.mktime(datetime.strptime(tw_date, "%a, %d %b %Y %H:%M:%S " + tw_lastpart).timetuple()) 
                    tw_timestamp = datetime.fromtimestamp(tw_timestamp) 
                    
                    print "    " + str(tweetcount) +': ' + tw[0] + " [-" + str(cur_timestamp - tw_timestamp) + "]"
                    tweetcount += 1
            else:
                for tw in userTweets[0:location]:
                    
                    tw_date = tw[1]
                    tw_lastpart = tw_date.split()[-1]
                    tw_timestamp = time.mktime(datetime.strptime(tw_date, "%a, %d %b %Y %H:%M:%S " + tw_lastpart).timetuple()) 
                    tw_timestamp = datetime.fromtimestamp(tw_timestamp)
                    
                    print "    " + str(tweetcount) +': ' + tw[0] + " [-" + str(cur_timestamp - tw_timestamp) + "]"
                    tweetcount += 1

            print userTweets[location][0]

            if location+5 < sizeoflist:
                for tw in userTweets[location+1:location+4]:
                    tw_date = tw[1]
                    tw_lastpart = str(tw_date.split()[-1])
                    tw_timestamp = time.mktime(datetime.strptime(tw_date, "%a, %d %b %Y %H:%M:%S " + tw_lastpart).timetuple()) 
                    tw_timestamp = datetime.fromtimestamp(tw_timestamp)
                    
                    print "    " + str(tweetcount) +': ' + tw[0] + " [" + str(tw_timestamp - cur_timestamp) + "]"
                    tweetcount += 1
            else:
                for tw in userTweets[location::sizeoflist]:
                    tw_date = tw[1]
                    tw_lastpart = str(tw_date.split()[-1])
                    tw_timestamp = time.mktime(datetime.strptime(tw_date, "%a, %d %b %Y %H:%M:%S " + tw_lastpart).timetuple()) 
                    tw_timestamp = datetime.fromtimestamp(tw_timestamp)   
                    
                    print "    " + str(tweetcount) +': ' + tw[0] + " [" + str(tw_timestamp - cur_timestamp) + "]"
                    tweetcount += 1

            
            print "[Distress:,Sad: ]"
            print "\n"


        globalTweet += 1     



def main():
    getuser_tweet_history()

if __name__ == '__main__':
    main()
    