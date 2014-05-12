import os, random
import cPickle as pickle
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from collections import defaultdict
from sklearn.decomposition import PCA


convertLables = { "H":-1, "ND":-1, "LD":1, "HD":1 }

def main():

    lhdfile = open("highdistressed.txt","rb")
    randfile = open("random_pick.txt", "rb")

    X = []
    y = [] 

    for line in lhdfile:

        X.append(line)
        y.append(1)

    for line in randfile:

        X.append(line)
        y.append(-1)


    
    vectorizer = TfidfVectorizer(analyzer='word', sublinear_tf=True, stop_words='english', ngram_range=(1,3), norm='l1', lowercase=True, use_idf=True, smooth_idf=True)
    X_train = vectorizer.fit_transform(X)

    pickle.dump(vectorizer,open("newvectorizer.pickle","wb"))

    X_train_arr = X_train.toarray()

    outfile1 = open('newsvmTrain.txt',"wb")


    for i in range(len(X_train_arr)):

        line =  str(y[i]) + " "

        # if int(y_train[i]) == 1 :
        #     line = line + "cost:0.60 "
        # else:
        #     line = line + "cost:0.40 "

        for value in range(len(X_train_arr[i])):

            if (float(X_train_arr[i][value]) != 0.0):                
                line = line + str(value+1) + ":" + str(X_train_arr[i][value]) + " "
    
        line = line + "\n"
        outfile1.write(line)  

    outfile1.close()
    

if __name__ == '__main__':
    main()


