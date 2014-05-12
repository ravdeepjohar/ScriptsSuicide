import pickle
import os

os.chdir("../")
traningDataset = pickle.load(open('outputs/train.pickle', "r"))
chris_labels = pickle.load(open("svm/mix_labels.pickle"))
convertLables = { "H":-1, "ND":-1 , "LD":1 , "HD":2 }


tweets = []
distressLabels = [] 

for key in traningDataset:
	
	if str(traningDataset[key][0]) in chris_labels:
		msg = ""
		#print str(traningDataset[key][0]), chris_labels[str(traningDataset[key][0])][0][0].rstrip(","), chris_labels[str(traningDataset[key][0])][0][1].rstrip("]") 
	   
		# for tweet in traningDataset[key][1]:
		# 	msg += tweet[0] + " "

		msg = traningDataset[key][1][3][0]
		tweets.append(msg)
		distressLabels.append(convertLables[chris_labels[str(traningDataset[key][0])][0][0].rstrip(",")])
	# print traningDataset[key][0]


for i in range(len(distressLabels)):

	#print distressLabels[i]

	if distressLabels[i] == 2:
		print tweets[i]