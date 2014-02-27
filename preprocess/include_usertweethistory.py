import sys, string, time, re, simplejson, os
from collections import defaultdict
from datetime import datetime
# from stemming.porter2 import stem
from nltk.corpus import wordnet
import cPickle as pickle

in_dict = { 'depressive_feelings' : ['me abused depressed', 'tired of living','so depressed','leave this world', 'wanna die','me hurt depressed', 'feel hopeless depressed', 'feel alone depressed', 'i feel helpless', 'i feel worthless', 'i feel sad', 'i feel empty', 'i feel anxious', 'hate my job', 'feeling guilty', 'deserve to die', 'desire to end own life', 'feeling ignored', 'tired of everything', 'feeling blue', 'have blues'], 'depression_symptoms' : ['sleeping pill','sleeping a lot', 'i feel irritable', 'i feel restless', 'have insomnia', 'sleep forever','sleep disorder'], 'drug_abuse' : ['depressed alcohol', 'sertraline', 'zoloft', 'prozac', 'pills depressed', 'clonazepam', 'drug overdose', 'imipramine'], 'prior_suicide_attempts' : ['suicide once more', 'me abused suicide', 'pain suicide', 'tried suicide'], 'suicide_around_individual' : ['mom suicide tried', 'sister suicide tried', 'brother suicide tried', 'friend suicide', 'suicide attempted', 'suicide attempt'], 'suicide_ideation' : ['commit suicide','committing suicide','feeling suicidal', 'suicide thought about', 'thoughts suicide', 'think suicide', 'thought killing myself', 'used thought suicide', 'once thought suicide', 'past thought suicide', 'multiple thought suicide', 'want to suicide', 'shoot myself', 'a gun to head', 'hang myself', 'intention to die'], 'self_harm' : ['stop cutting myself', 'hurt myself', 'cut myself'], 'bullying' : ['i am being bullied', 'i have been cyber bullied', 'was bullied', 'feel bullied', 'stop bullying me', 'keeps bullying me', 'always getting bullied'], 'gun_ownership' : ['gun suicide', 'shooting range went', 'gun range my'], 'psychological_disorders' : ['diagnosed schizophrenia', 'diagnosed anorexia', 'diagnosed bulimia', 'i diagnosed ocd', 'i diagnosed bipolar', 'i diagnosed ptsd', 'diagnosed borderline personality disorder', 'diagnosed panic disorder', 'diagnosed social anxiety disorder', 'diagnosed post traumatic stress disorder', 'sleep apnea'], 'family_violence_discord' : ['dad fight again', 'parents fight again', 'lost my friend', 'argument with wife', 'argument with husband', 'shouted at each other'], 'impulsivity' : ['i impulsive', 'i am impulsive'] }


def getuser_tweet_history ():

    os.chdir("../")
    dictionaryusers = pickle.load( open('outputs/usertweethistory.pickle', 'rb') )
    
    slang = dict()
    slangfile = open('preprocess/slang.txt','rb')

    for line in slangfile:
        sl = (line.rsplit("-",1)[0]).strip().lower()
        mean = (line.rsplit("-",1)[1]).strip().lower()
        #print sl + mean
        slang[sl] = mean   

    ditionary_include = dict()
    count = 0

    for user in dictionaryusers:

        userTweets =  dictionaryusers[user]
        sizeoflist = len(userTweets)

        for location in range(len(userTweets)):

            
            message = userTweets[location][0]
            usrtweet_msg_id = userTweets[location][2]
            usrtweet_date = str(userTweets[location][1])            

            lastpart = usrtweet_date.split()[-1]
            cur_timestamp = time.mktime(datetime.strptime(usrtweet_date, "%a, %d %b %Y %H:%M:%S " + lastpart).timetuple()) 
            cur_timestamp = datetime.fromtimestamp(cur_timestamp)

            
            nonSlangMessage = ""
            regexp = re.compile(r'\.[\.]+')
            nonDotMessage = ""

            for words in message.lower().split():
                if regexp.search(words) is not None:
                    nonDotMessage += re.sub(regexp, ' ', words) + " "
                    #print words
                else:
                    nonDotMessage += words + " "

            nonDotMessage = nonDotMessage[:-1]

            for words in nonDotMessage.lower().split():

                if not wordnet.synsets(words):
                    if words in slang:
                        nonSlangMessage += slang[words] + " "
                    else:
                        nonSlangMessage += words + " "
                else:
                    nonSlangMessage += words + " "


            nonSlangMessage = nonSlangMessage[:-1]

            suicidefactors= []

            for (key, value) in in_dict.iteritems():
                              
                for terms in value:
                    # split inclusive terms into single word combination
                    keywords = terms.split()
                    
                    # split messages into single word combination
                    words = nonSlangMessage.split()

                    # inclusive terms appear in original tweets, order does not matter
                    if len(set(keywords).intersection(set(words))) == len(keywords):
                        
                        suicidefactors.append(key)
                        break

            if len(suicidefactors) > 0:                

               
                tweet_list = []
                

                for loc in range(location-3,location+4):

                    if loc < 0:
                        cur_sadsum += 0 
                        tweet_list.append("N/A")
                        

                    elif loc > sizeoflist-1:
                        cur_sadsum += 0 
                        tweet_list.append("N/A")
                       
                    else:
                        tweet_list.append(userTweets[loc][0])

                include_tweet_info = [usrtweet_msg_id,tweet_list,sadavg, suicidefactors]
                  
                ditionary_include[count] = include_tweet_info
                count += 1 


    pickle.dump(ditionary_include, open('outputs/finalinclude.pickle' , 'wb'))

        
                
 
               

        
def main():
    getuser_tweet_history()

if __name__ == '__main__':
    main()
    