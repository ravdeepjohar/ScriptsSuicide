import os, random
import cPickle as pickle
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from collections import defaultdict
from sklearn.decomposition import PCA


convertLables = { "H":-1, "ND":-1, "LD":1, "HD":1 }

def main():

    trainingDataset = pickle.load(open('test.pickle', "r"))
    tweet_labels = pickle.load(open("mix_labels.pickle"))

    vectorizer = pickle.load(open("newvectorizer.pickle","rb"))

    tweets = []
    distressLabels = [] 

    for key in trainingDataset:
        
        if str(trainingDataset[key][0]) in tweet_labels:
            msg = ""
            #print str(trainingDataset[key][0]), tweet_labels[str(trainingDataset[key][0])][0][0].rstrip(","), tweet_labels[str(trainingDataset[key][0])][0][1].rstrip("]") 
            
            #for tweet in trainingDataset[key][1]:
                #msg += tweet[0] + " "
            #tweets.append(msg)
            tweets.append(trainingDataset[key][1][3][0])
            distressLabels.append(convertLables[tweet_labels[str(trainingDataset[key][0])][0][0].rstrip(",")])
        # print trainingDataset[key][0]
    # print len(tweets)
    # exit()

    outfile = open('newsvmTest.txt',"wb")

    pickle.dump(distressLabels,open("newtestlabels.pickle","wb"))

    for i in range(len(tweets)):

        line = tweets[i]
        label = distressLabels[i]

        X_test = vectorizer.transform([line.decode("utf-8")])
        X_test_arr = X_test.toarray()

        newline = str(label) + " "

        for index in range(len(X_test_arr[0])):

            if (float(X_test_arr[0,index]) != 0.0):
                newline = newline + str(index+1) + ":" + str(X_test_arr[0,index]) + " "

        newline = newline + "\n"

        outfile.write(newline)

    outfile.close()




if __name__ == '__main__':
    main()


