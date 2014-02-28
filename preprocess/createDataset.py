import re, string, os, sys, time
from datetime import datetime
from collections import defaultdict
import pickle, random


def createDataset():

	includeDict = pickle.load( open('finalinclude.pickle', 'rb') )
	sadDict = pickle.load( open('finalsad2.pickle', 'rb') )


	randIncludeDictKeys = random.choice(includeDict.keys())

	dataset1 = deafultdict(list)

	insertcount = 0 
	for key in randIncludeDictKeys:

		if (insertcount % 2 == 0):
			dataset1["include"].append(key)
		else:
			dataset2["include"].append(key)

		insertcount += 1 

	print len(dataset1["include"]), len(dataset2["include"])


	randSadDictKeys = random.choice(sadDict.keys())


	for i in range(1000-len(dataset1["include"]))
		dataset1["sad"].append(key)

	for i in range(1000-len(dataset1["include"]),1000-len(dataset1["include"])+100-len(dataset1["include"]))
		dataset2["sad"].append(key)







	
	datasetS1
	datasetI2
	datasetS2






def main():
	createDataset()


if __name__ == '__main__':
	main()