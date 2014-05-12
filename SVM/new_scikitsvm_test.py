import cPickle as pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import simplejson as json
import jsonpickle
from sklearn import svm, metrics
from sklearn.metrics import classification_report
import numpy as np

convertLables = { "H":-1, "ND":-1 , "LD":1 , "HD":1 }

def main():

    new_json = open("../test.json", "w")

    # count = 0 

    vectorizer = pickle.load(open("newvectorizer.pickle","rb"))

    clf1 = pickle.load(open("scikit_svm1.pickle","rb"))
    clf2 = pickle.load(open("scikit_svm2.pickle","rb"))
    clf3 = pickle.load(open("scikit_svm3.pickle","rb"))






#test begin
    # clf = pickle.load(open("scikit_svm2.pickle","rb"))

    # dataset = pickle.load(open('test.pickle', "r"))
    # tweet_labels = pickle.load(open("mix_labels.pickle"))

    # X_test = []
    # y_test = [] 

    # for key in dataset:
        
    #     if str(dataset[key][0]) in tweet_labels:

    #         X_test.append(dataset[key][1][3][0])
    #         y_test.append(convertLables[tweet_labels[str(dataset[key][0])][0][0].rstrip(",")])

    # X_test = vectorizer.transform(X_test) # a list goes in here

    # parameter = clf.get_params(deep=True)
    # print 'Classifier parameter:\n' + str(parameter)   

    # y_pred_class = []
    # y_value = []

    # for x in X_test:

    #     y_pred_class1 = clf.predict(x)[0]
    #     y_value1 = clf.decision_function(x)[0]

    #     y_pred_class.append(y_pred_class1)
    #     y_value.append(y_value1)

    # # confusion matrix
    # score = metrics.confusion_matrix(y_test, y_pred_class)
    # print 'Confusion Matrix:\n' + str(score)

    # # classification_report
    # print(classification_report(y_test, y_pred_class))

    # # AUC
    # y = np.array(y_test)
    # # pred = np.array(y_pred)
    # fpr, tpr, thresholds = metrics.roc_curve(y, y_pred_class)
    # roc_auc = metrics.auc(fpr,tpr)
    # print("Area under the ROC curve: %f" % roc_auc)
#test end












    # positivetweets = 0 
    # positivetweets1 = 0
    # positivetweets2 = 0


    for tweets_json in open("../nyc.trim.liwc", "r"):

        line = tweets_json.lower().strip()
        tweet = json.loads(line)
        message = tweet["doc"]["text"]


        #test_X = vectorizer.transform([line]) # 

        test_X = vectorizer.transform([message]) # 

        y_pred_class1 = clf1.predict(test_X)[0]
        y_value1 = clf1.decision_function(test_X)[0]

        y_pred_class2 = clf2.predict(test_X)[0]
        y_value2 = clf2.decision_function(test_X)[0]

        y_pred_class3 = clf3.predict(test_X)[0]
        y_value3 = clf3.decision_function(test_X)[0]

        # print y_pred_class1,y_pred_class2,y_pred_class3


        # if y_pred_class1 == 1:
        #     positivetweets += 1

        # if y_pred_class2 == 1:
        #     positivetweets1 += 1

        # if y_pred_class3 == 1:
        #     positivetweets2 += 1

                    
        tweet["doc"]["distress_result1"] = dict(classlabel = y_pred_class1, conf = y_value1)
        tweet["doc"]["distress_result2"] = dict(classlabel = y_pred_class2, conf = y_value2)
        tweet["doc"]["distress_result3"] = dict(classlabel = y_pred_class3, conf = y_value3)


        json.dump(tweet, new_json)
        new_json.write("\n")

        # if count>10:
        #     # print positivetweets, positivetweets1, positivetweets2 
        #     exit()
        # count += 1 

    new_json.close()


if __name__ == '__main__':
    main()