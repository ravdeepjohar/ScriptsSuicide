import pickle 
from random import uniform


def main():

	topicprob = [0.058, 0.069, 0.057, 0.107, 0.071, 0.055, 0.089, 0.091, 0.080, 0.051]
	topicprob.reverse()
	
	topicwordsfile = pickle.load(open('prob.pickle','rb')) 

	topicswords = []
	topicswordprob = []

	for line in topicwordsfile:
		
		line = line.split('+')
		words = []
		probs = []

		for word in line:
			word = word.split('*')

			words.append(word[1])
			probs.append(float(word[0]))

		topicswords.append(words)
		topicswordprob.append(probs)
	n= 500
	while n>0:
		generateSample(topicswords, topicswordprob, topicprob)
		n -= 1


def generateSample(topicswords,topicswordprob, topicprob):

	N = 10

	sample = ""

	while N>0:

		selectTopic = roulette(topicprob)

		word = roulette(topicswordprob[selectTopic])

		sample += topicswords[selectTopic][word]

		N -= 1

	print sample

def roulette(pro):

	su = 0

	for i in range(len(pro)):
		su += pro[i]

	p = uniform(0, su)

	j = 0
	index = 0

	while index < p:
		index += pro[j]
		j += 1

	return (j-2)




if __name__ == '__main__':
	main()