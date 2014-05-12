import os, random
import cPickle as pickle
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import svm, metrics
from collections import defaultdict
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.decomposition import PCA
import pylab as pl 
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report
import numpy as np
from sklearn.grid_search import GridSearchCV

convertLables = { "H":-1, "ND":-1 , "LD":1 , "HD":1 }

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


    trainingDataset = pickle.load(open('test.pickle', "r"))
    tweet_labels = pickle.load(open("mix_labels.pickle"))

    # vectorizer = pickle.load(open("newvectorizer.pickle","rb"))

    X_test = []
    y_test = [] 

    for key in trainingDataset:
        
        if str(trainingDataset[key][0]) in tweet_labels:
            msg = ""

            X_test.append(trainingDataset[key][1][3][0])
            y_test.append(convertLables[tweet_labels[str(trainingDataset[key][0])][0][0].rstrip(",")])


    vectorizer = TfidfVectorizer(analyzer='word', sublinear_tf=True, stop_words='english', ngram_range=(1,3), norm='l1', lowercase=True, use_idf=True, smooth_idf=True)
    X_train = vectorizer.fit_transform(X)
    X_test = vectorizer.transform(X_test)

    # pickle.dump(vectorizer,open("newvectorizer.pickle","wb"))

    X_train_arr = X_train.toarray()

    #weight_dict = { 1:10, -1:1 }

    # tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
    #                  'C': [1, 10, 100, 1000] ,'class_weight': [{ 1:1, -1:1 }, { 1:2, -1:1 }, { 1:5, -1:1 }, { 1:10, -1:1 }]},
    #                 {'kernel': ['linear'], 'C': [1, 10, 100, 1000], 'class_weight': [{ 1:1, -1:1 }, { 1:2, -1:1 }, { 1:5, -1:1 }, { 1:10, -1:1 }]}]

    # scores = ['precision', 'recall']

    # for score in scores:

    #     clf = GridSearchCV(svm.SVC(C=1,), tuned_parameters, cv=5, scoring=score)
    #     clf.fit(X_train, y)

    #     print("Best parameters set found on development set:")
    #     print()
    #     print(clf.best_estimator_)
    #     print()
    #     print("Grid scores on development set:")
    #     print()
    #     for params, mean_score, scores in clf.grid_scores_:
    #         print("%0.3f (+/-%0.03f) for %r"
    #               % (mean_score, scores.std() / 2, params))
    #     print()

    #     print("Detailed classification report:")
    #     print()
    #     print("The model is trained on the full development set.")
    #     print("The scores are computed on the full evaluation set.")
    #     print()
    #     y_true, y_pred = y_test, clf.predict(X_test)
    #     print(classification_report(y_true, y_pred))
    #     print()

    # exit()

    # SVC
    weight_dict1 = { 1:3, -1:1 }
    weight_dict2 = { 1:1, -1:3 }
    weight_dict3 = { 1:1, -1:1 }

    # # class_weight = weight_dict
    # # class_weight = 'auto'
    # clf1 = svm.LinearSVC(C = 100.0, class_weight = weight_dict1, loss = 'l2')
    # clf2 = svm.LinearSVC(C = 100.0, class_weight = weight_dict2, loss = 'l2')
    # clf3 = svm.LinearSVC(C = 100.0, class_weight = weight_dict3, loss = 'l2')

    clf = svm.LinearSVC(C = 100.0, class_weight = weight_dict3, loss = 'l1')
    
    # clf1.fit(X_train, y)
    # clf2.fit(X_train, y)
    # clf3.fit(X_train, y)

    clf.fit(X_train, y)


    # pickle.dump(clf1, open("scikit_svm1.pickle","wb"))
    # pickle.dump(clf2, open("scikit_svm2.pickle","wb"))
    # pickle.dump(clf3, open("scikit_svm3.pickle","wb"))
    

    parameter = clf.get_params(deep=True)
    print 'Classifier parameter:\n' + str(parameter)   

    y_pred = clf.predict(X_test)

    
    # confusion matrix
    score = metrics.confusion_matrix(y_test, y_pred)
    print 'Confusion Matrix:\n' + str(score)

    # classification_report
    print(classification_report(y_test, y_pred))

    # AUC
    y = np.array(y_test)
    # pred = np.array(y_pred)
    fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred)
    roc_auc = metrics.auc(fpr,tpr)
    print("Area under the ROC curve: %f" % roc_auc)

    # pl.clf()
    # pl.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
    # pl.plot([0, 1], [0, 1], 'k--')
    # pl.xlim([0.0, 1.0])
    # pl.ylim([0.0, 1.0])
    # pl.xlabel('False Positive Rate')
    # pl.ylabel('True Positive Rate')
    # pl.title('Receiver operating characteristic')
    # pl.legend(loc="lower right")
    # pl.show()

    
    

if __name__ == '__main__':
    main()


