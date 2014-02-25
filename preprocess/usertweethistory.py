import re, string, os, sys
from datetime import datetime
from collections import defaultdict
import cPickle as pickle




def getuser_tweet_history ():
    
   
    os.chdir("../")

    dictionaryusers = pickle.load( open('outputs/usertweethistory.pickle', 'rb') )
    suicideTweets = open('outputs/include.txt','r')

    for line in suicideTweets:

        userid = re.findall(r'\(\d*\)', line)       # 
        twee = re.findall(r'\([\d]*\)(.*)(AT)', line)
        time = re.findall(r'AT (.*)$', line)

        if userid and time:
            usrid = userid[0].strip('\(\)')            
            include_tweet = twee[0][0].strip(' --')
            userTweets = dictionaryusers[int(usrid)]
            sizeoflist = len(userTweets)
            userTweets.sort(key = lambda x : x.split(',')[1])
            location = -1

            for twee in range(0,len(userTweets)):

                thistweettimestamp = userTweets[twee].rsplit(',',1)[1]
                current_tweet = userTweets[twee].rsplit(',',1)[0]

                #Check if it is the same tweet and store location 

                if current_tweet == include_tweet:
                    location = twee

                # if thistweettimestamp == time[0]:
                #     print 'reached here!'
                #     location = twee

            # print the tweets 
            if location != -1: 

                if location-5 > 0:
                    for tw in userTweets[location-5:location]:
                        print tw.rsplit(',',1)[0]
                else:
                    for tw in userTweets[0:location]:
                        print tw.rsplit(',',1)[0]

                print "***" + userTweets[location].rsplit(',',1)[0]

                if location+5 < sizeoflist:
                    for tw in userTweets[location+1:location+6]:
                        print tw.rsplit(',',1)[0]
                else:
                    for tw in userTweets[location::sizeoflist]:
                        print tw.rsplit(',',1)[0]

                print "\n"
               

        #remove for whole dataset 
        # break


def main ():
    
    getuser_tweet_history()

         

if __name__ == "__main__":
    main()