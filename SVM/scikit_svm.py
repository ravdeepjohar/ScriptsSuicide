import os, random
import cPickle as pickle
# import logging, gensim, bz2
# from gensim import corpora, models, similarities
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import svm, metrics
from collections import defaultdict
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.decomposition import PCA
import pylab as pl 
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import AdaBoostClassifier

convertLables = { "H":-1, "ND":-1 , "LD":1 , "HD":1 }

def main():

    os.chdir("../")
    traningDataset = pickle.load(open('outputs/train.pickle', "r"))
    chris_labels = pickle.load(open("svm/megan_labels.pickle"))

    #existingLabels = defaultdict(list)


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
        # print traningDataset[key][0]

    X = tweets[200:]
    y_train = distressLabels[200:]
   
    testX = tweets[:200]
    y_test = distressLabels[:200]
 

    #sublinear_tf=True
    # vectorizer = TfidfVectorizer(sublinear_tf=True, stop_words='english',  ngram_range=(1,3) )
    #print vectorizer
    vectorizer = CountVectorizer(stop_words='english',  ngram_range=(1,3))

    X_train = vectorizer.fit_transform(X)
    X_test = vectorizer.transform(testX)

   
    # ch2 = SelectKBest(chi2)
    # X_train = ch2.fit_transform(X_train, y_train)
    # X_test = ch2.transform(X_test)


    # pca = PCA(n_components=15,  whiten=True)

    # X_train = pca.fit_transform(X_train.toarray())
    # X_test = pca.transform(X_test.toarray())

    weight_dict = { 1:1.5, -1:1 }

    # class_weight = weight_dict , 
    # clf = AdaBoostClassifier(n_estimators=50)

    clf = svm.SVC(class_weight = weight_dict, C = 10.0, kernel='linear', probability=True)
    
    clf.fit(X_train, y_train)   

    pred = clf.predict(X_test) 

    score = metrics.confusion_matrix(y_test,pred)   

    print score

    print metrics.f1_score(y_test,pred) 

    # pl.matshow(score)
    # pl.title('Confusion matrix')
    # pl.colorbar()
    # pl.ylabel('True label')
    # pl.xlabel('Predicted label')
    # pl.show()

   
    

if __name__ == '__main__':
    main()


