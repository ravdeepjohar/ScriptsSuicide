from collections import defaultdict 
import pickle 


def createDict(labelfile):

    filedict= defaultdict(list)

    for line in labelfile:

        line2 = line.split()

        # print line2[1], line2[3], line2[-2]

        if line2[3] == ", " or line2[-1] == "] ":
            print line

        else:
            filedict[line2[1]].append([line2[3],line2[-1]])
            
    return filedict




def main():

    labelfile = open("data_megan.txt","rb")

    # createDict(labelfile)

    pickle.dump(createDict(labelfile),open('megan_labels.pickle','wb'))




if __name__ == '__main__':
    main()