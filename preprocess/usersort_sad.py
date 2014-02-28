import re, string, os, sys, time
from datetime import datetime
from collections import defaultdict
import pickle



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
            noofNA = 0

            for loc in range(location-3,location+4):


                if loc < 0:
                    cur_sadsum += 0 
                    tweet_list.append(["N/A"," "])
                    noofNA += 1

                elif loc > sizeoflist-1:
                    cur_sadsum += 0 
                    tweet_list.append(["N/A"," "])
                    noofNA += 1

                else:

                    cur_sadsum += float(userTweets[loc][5])
                    tweet_list.append([userTweets[loc][0],str(userTweets[loc][1])])

            sadavg = cur_sadsum / 7.0 - float(noofNA)
            sad_tweet_info = [usrtweet_msg_id,tweet_list,sadavg, usrtweet_sadscore]


            if sadavg != 0.0:
                dicionarySadTweets[count] = sad_tweet_info
                count += 1

    print count

    finalsaddict = dict()
    nooftweets = 0

    for w in sorted(dicionarySadTweets, key = lambda x:float(dicionarySadTweets[x][3]), reverse=True):
       

        if(nooftweets < 20000): 
            finalsaddict[nooftweets] = dicionarySadTweets[w]

        nooftweets += 1

    pickle.dump(finalsaddict, open('outputs/finalsad2.pickle' , 'wb'))

    finalsaddict1 = dict()
    nooftweets = 0

    for w in sorted(finalsaddict, key = lambda x:float(finalsaddict[x][2]), reverse=True):
       

        if(nooftweets < 3000): 
            finalsaddict1[nooftweets] = finalsaddict[w]

        nooftweets += 1

    pickle.dump(finalsaddict1, open('outputs/finalsad.pickle' , 'wb'))


def main():
    sort_userTweetHistory()

if __name__ == '__main__':
    main()
    