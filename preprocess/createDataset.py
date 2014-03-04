import re, string, os, sys, time
from datetime import datetime
from collections import defaultdict
import pickle, random


def createDataset():

    includeDict = pickle.load( open('../outputs/finalinclude.pickle', 'rb') )
    sadDict = pickle.load( open('../outputs/finalsad2.pickle', 'rb') )


    randIncludeDictKeys = list(includeDict.keys())
    random.shuffle(randIncludeDictKeys)


    dataset1 = defaultdict(list)
    dataset2 = defaultdict(list)

    insertcount = 0 
    for key in randIncludeDictKeys:

        if (insertcount % 2 == 0):
            dataset1["include"].append(key)
        else:
            dataset2["include"].append(key)

        insertcount += 1 

    print len(dataset1["include"]), len(dataset2["include"])


    randSadDictKeys = list(sadDict.keys())
    random.shuffle(randSadDictKeys)

    for i in range(1000-len(dataset1["include"])):
        dataset1["sad"].append(randSadDictKeys[i])

    #print 1000-len(dataset1["include"])

    #print 1000-len(dataset1["include"])+1000-len(dataset1["include"])+1
    for i in range(1000-len(dataset1["include"])+1,1000-len(dataset1["include"])+1000-len(dataset1["include"])+1):
        dataset2["sad"].append(randSadDictKeys[i])

    print len(dataset1["sad"]), len(dataset2["sad"])


    data1 = open("dataset1.txt", "wb")
    data2 = open("dataset2.txt", "wb")

    data1count = 1
    data2count = 1

   

    for key in dataset1["include"]:

        date =  str(includeDict[key][1][3][1])

        #dataset1.write("
        print str(data1count) + ": Date:" , date  + " Category: " + str(includeDict[key][2][0])

        sillyCount = -3

        currentTweetDate = str(includeDict[key][1][3][1])
        lastpart = currentTweetDate.split()[-1]
        cur_timestamp = time.mktime(datetime.strptime(currentTweetDate, "%a, %d %b %Y %H:%M:%S " + lastpart).timetuple()) 
        cur_timestamp = datetime.fromtimestamp(cur_timestamp)

        for tweet in includeDict[key][1]:


            if str(tweet[1]) in " ":
                tw_date = str(includeDict[key][1][3][1])    
            else:
                tw_date = str(tweet[1])
                

            tw_lastpart = tw_date.split()[-1]
            tw_timestamp = time.mktime(datetime.strptime(tw_date, "%a, %d %b %Y %H:%M:%S " + tw_lastpart).timetuple()) 
            tw_timestamp = datetime.fromtimestamp(tw_timestamp) 


            if sillyCount in range(-3,0):
                
                print "    " + str(sillyCount) + ": " + tweet[0] + " [-" + str(cur_timestamp - tw_timestamp) + "]"

            if sillyCount == 0:
                print ">>> " + tweet[0] + " <<<"
                
            if sillyCount in range(1,4):
                print "     " + str(sillyCount) + ": " + tweet[0] + " [+" + str(tw_timestamp - cur_timestamp) + "]"

            sillyCount += 1

        print "Msg_id: " + str(includeDict[key][0]) + "  [Distress: , " + str(includeDict[key][2][0]) +": ]"
        print " "

        data1count += 1

    for key in dataset1["sad"]:

        date =  str(sadDict[key][1][3][1])
        lastpart = date.split()[-1]
        cur_timestamp = time.mktime(datetime.strptime(date, "%a, %d %b %Y %H:%M:%S " + lastpart).timetuple()) 
        cur_timestamp = datetime.fromtimestamp(cur_timestamp)

        #dataset1.write("
        print str(data1count) + ": Date:" , date  + " Category: LIWC Sad " 

        sillyCount = -3

        for tweet in sadDict[key][1]:

            if str(tweet[1]) in " ":
                tw_date = date
            else:
                tw_date = str(tweet[1])
                

            tw_lastpart = tw_date.split()[-1]
            tw_timestamp = time.mktime(datetime.strptime(tw_date, "%a, %d %b %Y %H:%M:%S " + tw_lastpart).timetuple()) 
            tw_timestamp = datetime.fromtimestamp(tw_timestamp) 

            if sillyCount in range(-3,0):
                print "    " + str(sillyCount) + ": " + tweet[0] + " [-" + str(cur_timestamp - tw_timestamp) + "]"

            if sillyCount == 0:
                print ">>> " + tweet[0] + " <<<"
                
            if sillyCount in range(1,4):
                print "     " + str(sillyCount) + ": " + tweet[0] + " [+" + str(tw_timestamp - cur_timestamp) + "]"

            sillyCount += 1

        print "Msg_id: " + str(sadDict[key][0]) + "  [Distress: , LIWC Sad: ]"
        print " "

        data1count += 1

    dataset1_2_include = dataset1["include"]
    random.shuffle(dataset1_2_include)
    dataset1_2_sad = dataset1["sad"]
    random.shuffle(dataset1_2_sad)

    data1count = 1
    data2count = 1

    for key in dataset1_2_include:

        date =  str(includeDict[key][1][3][1])

        #dataset1.write("
        print str(data1count) + ": Date:" , date  + " Category: " + str(includeDict[key][2][0])

        sillyCount = -3

        currentTweetDate = str(includeDict[key][1][3][1])
        lastpart = currentTweetDate.split()[-1]
        cur_timestamp = time.mktime(datetime.strptime(currentTweetDate, "%a, %d %b %Y %H:%M:%S " + lastpart).timetuple()) 
        cur_timestamp = datetime.fromtimestamp(cur_timestamp)

        for tweet in includeDict[key][1]:


            if str(tweet[1]) in " ":
                tw_date = str(includeDict[key][1][3][1])    
            else:
                tw_date = str(tweet[1])
                

            tw_lastpart = tw_date.split()[-1]
            tw_timestamp = time.mktime(datetime.strptime(tw_date, "%a, %d %b %Y %H:%M:%S " + tw_lastpart).timetuple()) 
            tw_timestamp = datetime.fromtimestamp(tw_timestamp) 


            if sillyCount in range(-3,0):
                
                print "    " + str(sillyCount) + ": " + tweet[0] + " [-" + str(cur_timestamp - tw_timestamp) + "]"

            if sillyCount == 0:
                print ">>> " + tweet[0] + " <<<"
                
            if sillyCount in range(1,4):
                print "     " + str(sillyCount) + ": " + tweet[0] + " [+" + str(tw_timestamp - cur_timestamp) + "]"

            sillyCount += 1

        print "Msg_id: " + str(includeDict[key][0]) + "  [Distress: , " + str(includeDict[key][2][0]) +": ]"
        print " "

        data1count += 1

    for key in dataset1_2_sad:

        date =  str(sadDict[key][1][3][1])
        lastpart = date.split()[-1]
        cur_timestamp = time.mktime(datetime.strptime(date, "%a, %d %b %Y %H:%M:%S " + lastpart).timetuple()) 
        cur_timestamp = datetime.fromtimestamp(cur_timestamp)

        #dataset1.write("
        print str(data1count) + ": Date:" , date  + " Category: LIWC Sad " 

        sillyCount = -3

        for tweet in sadDict[key][1]:

            if str(tweet[1]) in " ":
                tw_date = date
            else:
                tw_date = str(tweet[1])
                

            tw_lastpart = tw_date.split()[-1]
            tw_timestamp = time.mktime(datetime.strptime(tw_date, "%a, %d %b %Y %H:%M:%S " + tw_lastpart).timetuple()) 
            tw_timestamp = datetime.fromtimestamp(tw_timestamp) 

            if sillyCount in range(-3,0):
                print "    " + str(sillyCount) + ": " + tweet[0] + " [-" + str(cur_timestamp - tw_timestamp) + "]"

            if sillyCount == 0:
                print ">>> " + tweet[0] + " <<<"
                
            if sillyCount in range(1,4):
                print "     " + str(sillyCount) + ": " + tweet[0] + " [+" + str(tw_timestamp - cur_timestamp) + "]"

            sillyCount += 1

        print "Msg_id: " + str(sadDict[key][0]) + "  [Distress: , LIWC Sad: ]"
        print " "

        data1count += 1

    


    for key in dataset2["include"]:

        date =  str(includeDict[key][1][3][1])

        #dataset1.write("
        print str(data2count) + ": Date:" , date  + " Category: " + str(includeDict[key][2][0])

        sillyCount = -3

        currentTweetDate = str(includeDict[key][1][3][1])
        lastpart = currentTweetDate.split()[-1]
        cur_timestamp = time.mktime(datetime.strptime(currentTweetDate, "%a, %d %b %Y %H:%M:%S " + lastpart).timetuple()) 
        cur_timestamp = datetime.fromtimestamp(cur_timestamp)

        for tweet in includeDict[key][1]:


            if str(tweet[1]) in " ":
                tw_date = str(includeDict[key][1][3][1])    
            else:
                tw_date = str(tweet[1])
                

            tw_lastpart = tw_date.split()[-1]
            tw_timestamp = time.mktime(datetime.strptime(tw_date, "%a, %d %b %Y %H:%M:%S " + tw_lastpart).timetuple()) 
            tw_timestamp = datetime.fromtimestamp(tw_timestamp) 


            if sillyCount in range(-3,0):
                
                print "    " + str(sillyCount) + ": " + tweet[0] + " [-" + str(cur_timestamp - tw_timestamp) + "]"

            if sillyCount == 0:
                print ">>> " + tweet[0] + " <<<"
                
            if sillyCount in range(1,4):
                print "     " + str(sillyCount) + ": " + tweet[0] + " [+" + str(tw_timestamp - cur_timestamp) + "]"

            sillyCount += 1

        print "Msg_id: " + str(includeDict[key][0]) + "  [Distress: , " + str(includeDict[key][2][0]) +": ]"
        print " "

        data2count += 1

    for key in dataset2["sad"]:

        date =  str(sadDict[key][1][3][1])
        lastpart = date.split()[-1]
        cur_timestamp = time.mktime(datetime.strptime(date, "%a, %d %b %Y %H:%M:%S " + lastpart).timetuple()) 
        cur_timestamp = datetime.fromtimestamp(cur_timestamp)

        #dataset1.write("
        print str(data2count) + ": Date:" , date  + " Category: LIWC Sad " 

        sillyCount = -3

        for tweet in sadDict[key][1]:

            if str(tweet[1]) in " ":
                tw_date = date
            else:
                tw_date = str(tweet[1])
                

            tw_lastpart = tw_date.split()[-1]
            tw_timestamp = time.mktime(datetime.strptime(tw_date, "%a, %d %b %Y %H:%M:%S " + tw_lastpart).timetuple()) 
            tw_timestamp = datetime.fromtimestamp(tw_timestamp) 

            if sillyCount in range(-3,0):
                print "    " + str(sillyCount) + ": " + tweet[0] + " [-" + str(cur_timestamp - tw_timestamp) + "]"

            if sillyCount == 0:
                print ">>> " + tweet[0] + " <<<"
                
            if sillyCount in range(1,4):
                print "     " + str(sillyCount) + ": " + tweet[0] + " [+" + str(tw_timestamp - cur_timestamp) + "]"

            sillyCount += 1

        print "Msg_id: " + str(sadDict[key][0]) + "  [Distress: , LIWC Sad: ]"
        print " "

        data2count += 1

    dataset2_2_include = dataset2["include"]
    random.shuffle(dataset2_2_include)
    dataset2_2_sad = dataset2["sad"]
    random.shuffle(dataset2_2_sad)

    data1count = 1
    data2count = 1

    for key in dataset2_2_include:

        date =  str(includeDict[key][1][3][1])

        #dataset1.write("
        print str(data2count) + ": Date:" , date  + " Category: " + str(includeDict[key][2][0])

        sillyCount = -3

        currentTweetDate = str(includeDict[key][1][3][1])
        lastpart = currentTweetDate.split()[-1]
        cur_timestamp = time.mktime(datetime.strptime(currentTweetDate, "%a, %d %b %Y %H:%M:%S " + lastpart).timetuple()) 
        cur_timestamp = datetime.fromtimestamp(cur_timestamp)

        for tweet in includeDict[key][1]:


            if str(tweet[1]) in " ":
                tw_date = str(includeDict[key][1][3][1])    
            else:
                tw_date = str(tweet[1])
                

            tw_lastpart = tw_date.split()[-1]
            tw_timestamp = time.mktime(datetime.strptime(tw_date, "%a, %d %b %Y %H:%M:%S " + tw_lastpart).timetuple()) 
            tw_timestamp = datetime.fromtimestamp(tw_timestamp) 


            if sillyCount in range(-3,0):
                
                print "    " + str(sillyCount) + ": " + tweet[0] + " [-" + str(cur_timestamp - tw_timestamp) + "]"

            if sillyCount == 0:
                print ">>> " + tweet[0] + " <<<"
                
            if sillyCount in range(1,4):
                print "     " + str(sillyCount) + ": " + tweet[0] + " [+" + str(tw_timestamp - cur_timestamp) + "]"

            sillyCount += 1

        print "Msg_id: " + str(includeDict[key][0]) + "  [Distress: , " + str(includeDict[key][2][0]) +": ]"
        print " "

        data2count += 1

    for key in dataset2_2_sad:

        date =  str(sadDict[key][1][3][1])
        lastpart = date.split()[-1]
        cur_timestamp = time.mktime(datetime.strptime(date, "%a, %d %b %Y %H:%M:%S " + lastpart).timetuple()) 
        cur_timestamp = datetime.fromtimestamp(cur_timestamp)

        #dataset1.write("
        print str(data2count) + ": Date:" , date  + " Category: LIWC Sad " 

        sillyCount = -3

        for tweet in sadDict[key][1]:

            if str(tweet[1]) in " ":
                tw_date = date
            else:
                tw_date = str(tweet[1])
                

            tw_lastpart = tw_date.split()[-1]
            tw_timestamp = time.mktime(datetime.strptime(tw_date, "%a, %d %b %Y %H:%M:%S " + tw_lastpart).timetuple()) 
            tw_timestamp = datetime.fromtimestamp(tw_timestamp) 

            if sillyCount in range(-3,0):
                print "    " + str(sillyCount) + ": " + tweet[0] + " [-" + str(cur_timestamp - tw_timestamp) + "]"

            if sillyCount == 0:
                print ">>> " + tweet[0] + " <<<"
                
            if sillyCount in range(1,4):
                print "     " + str(sillyCount) + ": " + tweet[0] + " [+" + str(tw_timestamp - cur_timestamp) + "]"

            sillyCount += 1

        print "Msg_id: " + str(sadDict[key][0]) + "  [Distress: , LIWC Sad: ]"
        print " "

        data2count += 1







def main():
    createDataset()


if __name__ == '__main__':
    main()