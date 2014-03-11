import os, random
import cPickle as pickle
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from collections import defaultdict


convertLables = { "H":-1, "ND":-1 , "LD":1 , "HD":1 }

def main():

    os.chdir("../")
    traningDataset = pickle.load(open('outputs/train.pickle', "r"))
    chris_labels = pickle.load(open("svm/megan_labels.pickle"))

 
    tweets = []
    distressLabels = [] 

    for key in traningDataset:
        
        if str(traningDataset[key][0]) in chris_labels:
            msg = ""
            #print str(traningDataset[key][0]), chris_labels[str(traningDataset[key][0])][0][0].rstrip(","), chris_labels[str(traningDataset[key][0])][0][1].rstrip("]") 
            
            for tweet in traningDataset[key][1]:
                msg += tweet[0] + " "
            tweets.append(msg)
            distressLabels.append(convertLables[chris_labels[str(traningDataset[key][0])][0][0].rstrip(",")])
        #print traningDataset[key][0]

    
    X = tweets[200:]    
    y_train = distressLabels[200:]    

    testX = tweets[:200]
    y_test = distressLabels[:200]

    # for tf-idf
    vectorizer = TfidfVectorizer(sublinear_tf=True, stop_words='english',  ngram_range=(1,3) )
    # for word count
    #vectorizer = CountVectorizer(stop_words='english',  ngram_range=(1,3))

    X_train = vectorizer.fit_transform(X)
    X_test = vectorizer.transform(testX)

    X_train_arr = X_train.toarray()
    X_test_arr = X_test.toarray()

    outfile1 = open('svm/traindataforSVM.txt',"wb")
    outfile2 = open('svm/testdataforSVM.txt',"wb")
    

    for i in range(10):#len(X_train_arr)):

        line =  str(y_test[i]) + " "

        for tfidf in range(len(X_train_arr[i])):
            line = line + str(tfidf+1) + ":" + str(X_train_arr[i][tfidf]) + " "
        line = line + "\n"
        outfile1.write(line)  

    exit() 
   
    for i in range(len(X_test_arr)):

        line =  str(y_test[i]) + " "

        for tfidf in range(len(X_test_arr[i])):
            line = line + str(tfidf+1) + ":" + str(X_test_arr[i][tfidf]) + " "
        line = line + "\n"
        outfile2.write(line)
  

    outfile1.close()
    outfile2.close()
    

if __name__ == '__main__':
    main()


