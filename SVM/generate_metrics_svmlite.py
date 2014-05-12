from sklearn.metrics import classification_report, confusion_matrix
import pickle
import pylab as pl 
import numpy as np
from sklearn import metrics

def main():
    # modelfile = open('svm_light/model.txt', "rb")
    # model = []

    # for line in modelfile:
    #     model.append(line)

    # pickle.dump(model, open('SVM_model.pickle',"wb"))


    # test dataset
    y_test_pic = pickle.load(open('newtestlabels.pickle',"rb"))

    y_test = []
    for val in y_test_pic:
        y_test.append(val)
        
    # prediction result
    predfile = open('svm_light/newprediction.txt', "rb")

    pred = [] 

    for val in predfile:

        val = float(val)
       
        if val > 0.0:
            pred.append(1)
        else:
            pred.append(-1)

    # report
    score = confusion_matrix(y_test, pred)
    print 'Confusion Matrix:\n' + str(score)
    print(classification_report(y_test, pred))

    # Compute ROC curve and area the curve
    fpr, tpr, thresholds = metrics.roc_curve(y_test, pred)
    roc_auc = metrics.auc(fpr,tpr)
    print("Area under the ROC curve: %f" % roc_auc)

    # Plot ROC curve
    pl.clf()
    pl.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
    pl.plot([0, 1], [0, 1], 'k--')
    pl.xlim([0.0, 1.0])
    pl.ylim([0.0, 1.0])
    pl.xlabel('False Positive Rate')
    pl.ylabel('True Positive Rate')
    pl.title('Receiver Operating Characteristic')
    pl.legend(loc="lower right")
    pl.show()


if __name__ == '__main__':
    main()

