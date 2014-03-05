import re, string, os, sys, time
from datetime import datetime
from collections import defaultdict
import pickle





def main():

    os.chdir("../")
    dictionaryusers = pickle.load( open('outputs/usertweethistory.pickle', 'rb'))
    trainfile = open('data/train.txt','rb')

    train = []

    for msg in trainfile:

        train.append(msg)

    traindict = dict()

    count = 0

    for user in dictionaryusers:

        userTweets =  dictionaryusers[user]
        sizeoflist = len(userTweets)

        for location in range(len(userTweets)):

            message = userTweets[location][0]
            usrtweet_msg_id = userTweets[location][2]
            usrtweet_date = str(userTweets[location][1]) 
            usrtweet_negemo = str(userTweets[location][4]) 
            usrtweet_sadscore =  float(userTweets[location][5])     

            lastpart = usrtweet_date.split()[-1]
            cur_timestamp = time.mktime(datetime.strptime(usrtweet_date, "%a, %d %b %Y %H:%M:%S " + lastpart).timetuple()) 
            cur_timestamp = datetime.fromtimestamp(cur_timestamp)

            cur_sadsum = 0 
            tweet_list = []
            noofNA = 0

            if usrtweet_msg_id in train:

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
                tweet_info = [usrtweet_msg_id,tweet_list,sadavg, usrtweet_sadscore, usrtweet_negemo]

                traindict[count] = tweet_info
                count += 1


    pickle.dump(finalsaddict1, open('outputs/train.pickle' , 'wb'))



if __name__ == '__main__':
    main()