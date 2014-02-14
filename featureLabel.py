import sys
import simplejson
from datetime import datetime
import math
from collections import defaultdict
import re
import string


in_dict = { 'depressive_feelings' : ['me abused depressed', 'me hurt depressed', 'feel hopeless depressed', 'feel alone depressed', 'i feel helpless', 'i feel worthless', 'i feel sad', 'i feel empty', 'i feel anxious'], 'depression_symptoms' : ['sleeping a lot lately', 'i feel irritable', 'i feel restless'], 'drug_abuse' : ['depressed alcohol', 'sertraline', 'zoloft', 'prozac', 'pills depressed'], 'prior_suicide_attempts' : ['suicide once more', 'me abused suicide', 'pain suicide', 'i have tried suicide before'], 'suicide_around_individual' : ['mom suicide tried', 'sister suicide tried', 'brother suicide tried', 'friend suicide', 'suicide attempted sister'], 'suicide_ideation' : ['suicide thought about before', 'thought suicide before', 'had thoughts suicide', 'had thoughts killing myself', 'used thoughts suicide', 'once thought suicide', 'past thoughts suicide', 'multiple thought suicide'], 'self_harm' : ['stop cutting myself'], 'bullying' : ['i am being bullied', 'i have been cyber bullied', 'feel bullied i am', 'stop bullying me', 'keeps bullying me', 'always getting bullied'], 'gun_ownership' : ['gun suicide', 'shooting range went', 'gun range my'], 'psychological_disorders' : ['i was diagnosed schizophrenia', 'been diagnosed anorexia', 'diagnosed bulimia', 'i diagnosed ocd', 'i diagnosed bipolar', 'i diagnosed ptsd', 'diagnosed borderline personality disorder', 'diagnosed panic disorder', 'diagnosed social anxiety disorder'], 'family_violence_discord' : ['dad fight again', 'parents fight again'], 'impulsivity' : ['i impulsive', 'i am impulsive'] }

ex_dict = { 'feel alone depressed' : ['cockroach', '364'], 'i feel helpless' : ['when', 'without','girl'], 'i feel sad' : ['epidose', 'when', 'lakers', 'about', 'game', 'you', 'sorry', 'for', 'bad', 'bieber'], 'i feel empty' : ['stomach', 'phone', 'hungry', 'food'], 'sleeping a lot lately' : ['have not been'], 'i feel irritable' : ['was'], 'depressed' : ['ronan'], 'sertraline' : ['special class', 'viagra', 'study', 'clinical', 'http'], 'zoloft' : ['toma', 'para', 'necesito', 'siempre', 'gracioso', 'desde', 'decirle', 'palabra', 'vida', 'sabor', 'aborto', 'gusta'], 'prozac' : ['toma', 'para', 'necesito', 'siempre', 'gracioso', 'desde', 'decirle', 'palabra', 'vida', 'sabor', 'aborto', 'gusta'], 'pills depressed' : ['http'], 'suicide once more' : ['will', 'by', 'live'], 'pain suicide' : ['http'], 'mom suicide tried' : ['dog', 'cat', 'fish', 'who'], 'sister suicide tried' : ['dog', 'cat', 'fish'], 'brother suicide tried' : ['dog', 'cat', 'fish', 'big brother'], 'friend suicide' : ['hold still'], 'suicide attempted sister' : ['paperback'], 'thought suicide before' : ['http'], 'had thoughts suicide' : ['http', 'never'], 'had thoughts killing myself' : ['not'], 'stop cutting myself' : ['off', 'shaving', 'hair', 'shave', 'slack', 'accidentally'], 'i am being bullied' : ['straightophobic'], 'feel bullied i am' : ['lol'], 'stop bullying me' : ['#stop'], 'always getting bullied' : ['lol'], 'gun suicide' : ['zimmerman', 'news', 'you', 'water', 'nerf'], 'been diagnosed anorexia' : ['http'], 'i diagnosed ocd' : ['never', 'cdo', 'check'], 'i diagnosed bipolar' : ['not'], 'dad fight again' : ['food'], 'parents fight again' : ['sartan', 'bradley', 'pacquiao', 'gas'], 'i impulsive' : ['clementine'], 'i am impulsive' : ['clementine'] }

def label_feature (twitter_file):
	"Labels Twitter data with features"

	# initialize a counter for inclusion terms
	counts = dict()
	for (key, value) in in_dict.iteritems():
		counts[key] = 0

	# open the data file
	tweets_json = open(twitter_file)

	# initialize a counter for tweets to test
	count = 0
	
	while True:
		# pre-process data
		line = tweets_json.readline().lower().strip()
		
		# set the limit to test
		count += 1

		#Comment this part to run for entire dataset
		
		if count > 100000:
			break

		# TO run whole dataset
		# if not line:
			# break

		tweet = simplejson.loads (line)
		
		# read each text message
		message = tweet["doc"]["text"].encode("utf-8")
		
		for (key, value) in in_dict.iteritems():
			# initialize new attributes (suicide risk factors)
			tweet[key] = 0

			# inclusive terms
			for terms in value:
				# split inclusive terms into single word combination
				keywords = terms.split()
				
				# split messages into single word combination
				words = message.split()

				# inclusive terms appear in original tweets, order does not matter
				if len(set(keywords).intersection(set(words))) == len(keywords):
					# change the flag
					tweet[key] = 1

					# update the counter
					counts[key] += 1

					# exclude and turn flag back to 0
					for (k, v) in ex_dict.iteritems():
						for term in v:
							t = term.split()

							if len(set(t).intersection(set(words))) == len(t):
								tweet[key] = 0
								counts[key] -= 1			
					

					# print filtered results
					print message


		outline = simplejson.dumps(tweet)
		
	print counts

def main ():

	# label_feature("m_NYC_all.json")
	label_feature("nyc.trim.liwc")

		 

if __name__ == "__main__":
	main()