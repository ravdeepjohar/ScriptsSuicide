import re, string, os, sys, time
from datetime import datetime
from collections import defaultdict
import cPickle as pickle



def sort_userTweetHistory():

    os.chdir("../")
    dictionaryusers = pickle.load( open('outputs/usertweethistory.pickle', 'rb'))

    dicionarySadTweets = dict()
    count = 0

    for user in dictionaryusers:

        userTweets =  dictionaryusers[user]
        sizeoflist = len(userTweets)

        for location in range(len(userTweets)):


            message = userTweets[location][0]
            usrtweet_msg_id = userTweets[location][2]
            usrtweet_date = str(userTweets[location][1]) 
            usrtweet_sadscore =  float(userTweets[location][5])     

            lastpart = usrtweet_date.split()[-1]
            cur_timestamp = time.mktime(datetime.strptime(usrtweet_date, "%a, %d %b %Y %H:%M:%S " + lastpart).timetuple()) 
            cur_timestamp = datetime.fromtimestamp(cur_timestamp)

            cur_sadsum = 0 
            tweet_list = []


            for loc in range(location-3,location+4):


                if loc < 0:
                    cur_sadsum += 0 
                    tweet_list.append["N/A"]

                elif loc > sizeoflist:
                    cur_sadsum += 0 
                    tweet_list.append["N/A"]

                else:

                    cur_sadsum += float(userTweets[loc][5])
                    tweet_list.append(userTweets[loc][0])

            sadavg = tweet_list/7
            sad_tweet_info = [usrtweet_msg_id,tweet_list,sadavg]


            print sad_tweet_info

            break
        break=













             


def main():
    sort_userTweetHistory()

if __name__ == '__main__':
    main()
    