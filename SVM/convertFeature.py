import os, pickle
from sklearn.feature_extraction.text import TfidfVectorizer


def vectorizer(alldata):

    outfile = open('SVM/alldata.txt', "wb")

    file1 = open('SVM/tfidf_vectorizer.pickle', "rb")

    X_train_arr = pickle.load(file1)
    vectorizer = pickle.load(file1)

    file1.close()

    # counter = 0

    for line in alldata:

        # if counter <= 10:

        X_test = vectorizer.transform([line.decode("utf-8")])
        X_test_arr = X_test.toarray()

        newline = "1 "

        for index in range(len(X_test_arr[0])):

            if (float(X_test_arr[0,index]) != 0.0):
                newline = newline + str(index+1) + ":" + str(X_test_arr[0,index]) + " "

        newline = newline + "\n"

        outfile.write(newline)
        # counter += 1

    outfile.close()


def main():

    os.chdir("../")
    alldata = open('outputs/tweets.txt', "rb")

    vectorizer(alldata)


if __name__ == '__main__':
    main()