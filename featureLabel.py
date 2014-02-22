import sys, string, time, pickle, re, simplejson
from collections import defaultdict
from datetime import datetime
# from stemming.porter2 import stem
from nltk.corpus import wordnet


in_dict = { 'depressive_feelings' : ['me abused depressed', 'me hurt depressed', 'feel hopeless depressed', 'feel alone depressed', 'i feel helpless', 'i feel worthless', 'i feel sad', 'i feel empty', 'i feel anxious', 'hate my job', 'feeling guilty', 'deserve to die', 'desire to end own life', 'feeling ignored', 'tired of everything'], 'depression_symptoms' : ['sleeping a lot', 'i feel irritable', 'i feel restless', 'have insomnia', 'sleep disorder'], 'drug_abuse' : ['depressed alcohol', 'sertraline', 'zoloft', 'prozac', 'pills depressed', 'clonazepam', 'drug overdose', 'imipramine'], 'prior_suicide_attempts' : ['suicide once more', 'me abused suicide', 'pain suicide', 'tried suicide'], 'suicide_around_individual' : ['mom suicide tried', 'sister suicide tried', 'brother suicide tried', 'friend suicide', 'suicide attempted', 'suicide attempt'], 'suicide_ideation' : ['feeling suicidal', 'suicide thought about', 'thoughts suicide', 'think suicide', 'thought killing myself', 'used thought suicide', 'once thought suicide', 'past thought suicide', 'multiple thought suicide', 'want to suicide', 'shoot myself', 'a gun to head', 'hang myself', 'intention to die'], 'self_harm' : ['stop cutting myself', 'hurt myself', 'cut myself'], 'bullying' : ['i am being bullied', 'i have been cyber bullied', 'was bullied', 'feel bullied', 'stop bullying me', 'keeps bullying me', 'always getting bullied'], 'gun_ownership' : ['gun suicide', 'shooting range went', 'gun range my'], 'psychological_disorders' : ['diagnosed schizophrenia', 'diagnosed anorexia', 'diagnosed bulimia', 'i diagnosed ocd', 'i diagnosed bipolar', 'i diagnosed ptsd', 'diagnosed borderline personality disorder', 'diagnosed panic disorder', 'diagnosed social anxiety disorder', 'diagnosed posttraumatic stress disorder', 'sleep apnea'], 'family_violence_discord' : ['dad fight again', 'parents fight again', 'lost my friend', 'argument with wife', 'argument with husband', 'shouted at each other'], 'impulsivity' : ['i impulsive', 'i am impulsive'] }

ex_dict = { 'feel alone depressed' : ['cockroach', '364'], 'i feel helpless' : ['when', 'without','girl'], 'i feel sad' : ['epidose', 'when', 'lakers', 'about', 'game', 'you', 'sorry', 'for', 'bad', 'bieber'], 'i feel empty' : ['stomach', 'phone', 'hungry', 'food'], 'sleeping a lot lately' : ['have not been'], 'i feel irritable' : ['was'], 'depressed' : ['ronan'], 'sertraline' : ['special class', 'viagra', 'study', 'clinical', 'http'], 'zoloft' : ['toma', 'para', 'necesito', 'siempre', 'gracioso', 'desde', 'decirle', 'palabra', 'vida', 'sabor', 'aborto', 'gusta'], 'prozac' : ['toma', 'para', 'necesito', 'siempre', 'gracioso', 'desde', 'decirle', 'palabra', 'vida', 'sabor', 'aborto', 'gusta'], 'pills depressed' : ['http'], 'suicide once more' : ['will', 'by', 'live'], 'pain suicide' : ['http'], 'mom suicide tried' : ['dog', 'cat', 'fish', 'who'], 'sister suicide tried' : ['dog', 'cat', 'fish'], 'brother suicide tried' : ['dog', 'cat', 'fish', 'big brother'], 'friend suicide' : ['hold still'], 'suicide attempted sister' : ['paperback'], 'thought suicide before' : ['http'], 'had thoughts suicide' : ['http', 'never'], 'had thoughts killing myself' : ['not'], 'stop cutting myself' : ['off', 'shaving', 'hair', 'shave', 'slack', 'accidentally'], 'i am being bullied' : ['straightophobic'], 'feel bullied i am' : ['lol'], 'stop bullying me' : ['#stop'], 'always getting bullied' : ['lol'], 'gun suicide' : ['zimmerman', 'news', 'you', 'water', 'nerf'], 'been diagnosed anorexia' : ['http'], 'i diagnosed ocd' : ['never', 'cdo', 'check'], 'i diagnosed bipolar' : ['not'], 'dad fight again' : ['food'], 'parents fight again' : ['sartan', 'bradley', 'pacquiao', 'gas'], 'i impulsive' : ['clementine'], 'i am impulsive' : ['clementine'] }

f1 = open('outputs/exclude.txt', 'w+')
f2 = open('outputs/include.txt', 'w+')

def label_feature (twitter_file):
    "Labels Twitter data with features"

    dictionaryusers = defaultdict(list)

    slang = dict()
    slangfile = open('preprocess/slang.txt','rb')
    for line in slangfile:
        sl = (line.rsplit("-",1)[0]).strip().lower()
        mean = (line.rsplit("-",1)[1]).strip().lower()
        #print sl + mean
        slang[sl] = mean

    # initialize a counter for inclusion terms
    counts = dict()
    for (key, value) in in_dict.iteritems():
        counts[key] = 0

    # open the data file
    tweets_json = open(twitter_file)

    # initialize a counter for tweets to test
    count = 0
    
    while True:
        # pre-process data
        line = tweets_json.readline().lower().strip()
        

        # comment this part to run for entire dataset
        # count += 1
        # if count > 100000:
        #     break

        # TO run whole dataset
        if not line:
            break

        tweet = simplejson.loads (line)
        
        # read each text message
        message = tweet["doc"]["text"].encode("utf-8")
        #stemmedMessage = stem(message)
        
        # stemmedMessage = ""
        # for words in message.split():
        #     stemmedMessage += stem(words) + " "
        # print stemmedMessage

        # print "------"

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

        message = nonSlangMessage
    
        
        from_user = tweet["doc"]["from_user"]
        from_user_id = tweet["doc"]["from_user_id"]
        created_at = tweet["doc"]["created_at"]
        lastpart = created_at.split()[-1]
        convertedDate = time.mktime(datetime.strptime(created_at, "%a, %d %b %Y %H:%M:%S " + lastpart).timetuple()) 
        info = message + ',' + str(convertedDate)

        # Add tweets in dictionary 
        dictionaryusers[from_user_id].append(info)

        
        for (key, value) in in_dict.iteritems():
            # initialize new attributes (suicide risk factors)
            tweet[key] = 0

            # inclusive terms
            for terms in value:
                # split inclusive terms into single word combination
                keywords = terms.split()
                
                # split messages into single word combination
                words = message.split()

                # inclusive terms appear in original tweets, order does not matter
                if len(set(keywords).intersection(set(words))) == len(keywords):
                    # change the flag
                    tweet[key] = 1

                    excludeflag = 0 

                    # exclude and turn flag back to 0
                    for (k, v) in ex_dict.iteritems():
                        for term in v:
                            t = term.split()

                            if len(set(t).intersection(set(words))) == len(t):
                                tweet[key] = 0
                                excludeflag = 1
                                f1.write("[" + key + "]--" + from_user + "(" + str(from_user_id) + ")--" + message + " AT " + str(convertedDate) + "\n")

                     # update the counter

                    if excludeflag == 0:
                        counts[key] += 1
                        # print filtered results
                        f2.write("[" + key + "]--" + from_user + "(" + str(from_user_id) + ")--" + message + " AT " + str(convertedDate) + "\n")

        outline = simplejson.dumps(tweet)
        
    f2.write(str(counts))
    #pickle.dump(dictionaryusers, open('outputs/usertweethistory.pickle' , 'w'))

# f1.close()
# f2.close()

def main ():

    label_feature("nyc.trim.liwc")

         

if __name__ == "__main__":
    main()
