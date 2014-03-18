import time
import string
import os
import sys
#import system as sys
### OUTPUT
# 1 first_person,
# 2 second_person
# 3 third_person
# 4 posemo
# 5 negemo
# 6 cognitive,
# 7 sensory
# 8 time
# 9 past
# 10 present
# 11 future
# 12 work
# 13 leisure
# 14 swear
# 15 social
# 16 family
# 17 friend
# 18 humans
# 19 anx
# 20 anger
# 21 sad
# 22 body
# 23 health
# 24 sexual
# 25 space
# 26 time
# 27 achieve
# 28 home
# 29 money
# 30 relig
# 31 Affect
# 32 cause
# 33 Quant
# 34 Numb
# 35 inhib
# 36 ingest
# 37 motion
# 38 nonfl
# 39 filler
# 40 number_classified_words
# 41 number_words



# read in liwc data file
# cat = list of categories,
# dic = list of all words with categories
def read_liwc(filename):
  liwc_data = open(os.path.join(os.path.dirname(__file__),filename), "r")
  mode = 0
  cat = {}
  dic = {}

  for line in liwc_data:
    line = line.strip("\r\n")
    if line == "%":
      mode += 1
      continue
    #load the categories first
    elif mode == 1:
      chunks = line.split("\t")
      #e.g., cat['133']='cause'
      cat[chunks[0]] = chunks[1]

    # then load words for each category
    elif mode == 2:
      chunks = line.split("\t")
      word = chunks.pop(0)
      #e.g., dic['affect']=[131,133]
      dic[word] = chunks

  return (cat,dic)

def get_wordsets(dic):
  first_person={}
  second_person={}
  third_person={}
  posemo = {}
  negemo = {}
  cognitive={}
  sensory={}
  time={}
  past={}
  present={}
  future={}
  work={}
  leisure={}
  swear={}
  social={}
  family={}
  friend={}
  humans={}
  anx={}
  anger={}
  sad={}
  body={}
  health={}
  sex={}
  space={}
  time={}
  achieve={}
  home={}
  money={}
  religion={}
  affect={}
  cause={}
  quant={}
  numb={}
  inhib={}
  ingst={}
  motion={}
  nonfl={}
  filler={}
  for word in dic:
    ### 1.
    for cat in dic[word]:
      if cat in ['4', '5']:
        first_person[word] = dic[word]
        continue
    ### 2.
    for cat in dic[word]:
    	if cat in ['6']:
    		second_person[word] = dic[word]
    		continue
    ### 3.
    for cat in dic[word]:
    	if cat in ['7', '8']:
    		third_person[word] = dic[word]
    		continue
    ### 4.
    for cat in dic[word]:
    	if cat in ['126']:
        #e.g., posemo['accept']= [125, 126, ]
    		posemo[word] = dic[word]
    		continue
    ### 5.
    for cat in dic[word]:
    	if cat in ['19', '127', '128', '129', '130']:
    		negemo[word] = dic[word]
    		continue
    ### 6.
    for cat in dic[word]:
    	if cat in ['131', '132', '133', '134', '135', '136', '137', '138', '139']:
    		cognitive[word] = dic[word]
    		continue
    ### 7.
    for cat in dic[word]:
    	if cat in ['140', '141', '142', '143']:
    		sensory[word] = dic[word]
    		continue
    ### 8.
    for cat in dic[word]:
    	if cat in ['253']:
    		time[word] = dic[word]
    		continue
    ### 9.
    for cat in dic[word]:
    	if cat in ['13']:
    		past[word] = dic[word]
    		continue
    ### 10.
    for cat in dic[word]:
    	if cat in ['14']:
    		present[word] = dic[word]
    		continue
    ### 11.
    for cat in dic[word]:
    	if cat in ['15']:
    		future[word] = dic[word]
    		continue
    ### 12.
    for cat in dic[word]:
    	if cat in ['354']:
    		work[word] = dic[word]
    		continue
    ### 13.
    for cat in dic[word]:
    	if cat in ['356']:
    		leisure[word] = dic[word]
    		continue
    ### 14.
    for cat in dic[word]:
    	if cat in ['22']:
    		swear[word] = dic[word]
    		continue
    ### 15.
    for cat in dic[word]:
    	if cat in ['121']:
    		social[word] = dic[word]
    		continue
    ### 16.
    for cat in dic[word]:
    	if cat in ['122']:
    		family[word] = dic[word]
    		continue
    ### 17.
    for cat in dic[word]:
    	if cat in ['123']:
    		friend[word] = dic[word]
    		continue
    ### 18.
    for cat in dic[word]:
    	if cat in ['124']:
    		humans[word] = dic[word]
    		continue
    ### 19.
    for cat in dic[word]:
    	if cat in ['128']:
    		anx[word] = dic[word]
    		continue
    ### 20.
    for cat in dic[word]:
    	if cat in ['129']:
    		anger[word] = dic[word]
    		continue
    ### 21.
    for cat in dic[word]:
    	if cat in ['130']:
    		sad[word] = dic[word]
    		continue
    ### 22.
    for cat in dic[word]:
    	if cat in ['147']:
    		body[word] = dic[word]
    		continue
    ### 23.
    for cat in dic[word]:
    	if cat in ['148']:
    		health[word] = dic[word]
    		continue
    ### 24.
    for cat in dic[word]:
    	if cat in ['149']:
    		sex[word] = dic[word]
    		continue
    ### 25.
    for cat in dic[word]:
    	if cat in ['252']:
    		space[word] = dic[word]
    		continue
    ### 26.
    for cat in dic[word]:
    	if cat in ['253']:
    		time[word] = dic[word]
    		continue
    ### 27.
    for cat in dic[word]:
    	if cat in ['355']:
    		achieve[word] = dic[word]
    		continue
    ### 28.
    for cat in dic[word]:
    	if cat in ['357']:
    		home[word] = dic[word]
    		continue
    ### 29.
    for cat in dic[word]:
    	if cat in ['358']:
    		money[word] = dic[word]
    		continue
    ### 30.
    for cat in dic[word]:
    	if cat in ['359']:
    		religion[word] = dic[word]
    		continue
    ### 31.
    for cat in dic[word]:
      if cat in ['125']:
        affect[word] = dic[word]
        continue
    ### 32.
    for cat in dic[word]:
      if cat in ['133']:
        cause[word] = dic[word]
        continue
    ### 33.
    for cat in dic[word]:
      if cat in ['20']:
        quant[word] = dic[word]
        continue
    ### 34.
    for cat in dic[word]:
    	if cat in ['21']:
    		numb[word] = dic[word]
    		continue
    ### 35.
    for cat in dic[word]:
    	if cat in ['137']:
    		inhib[word] = dic[word]
    		continue
    ### 36.
    for cat in dic[word]:
    	if cat in ['150']:
    		ingst[word] = dic[word]
    		continue
    ### 37.
    for cat in dic[word]:
    	if cat in ['251']:
    		motion[word] = dic[word]
    		continue
    ### 38.
    for cat in dic[word]:
    	if cat in ['463']:
    		nonfl[word] = dic[word]
    		continue
    ### 39.
    for cat in dic[word]:
    	if cat in ['464']:
    		filler[word] = dic[word]
    		continue
  return (first_person, second_person, third_person, posemo, negemo, cognitive, sensory, time, past, present, future, work,leisure,swear, social, family, friend, humans, anx, anger, sad, body, health, sex, space, time, achieve, home, money, religion,affect,cause,quant,numb,inhib,ingst,motion,nonfl,filler)


def matches(liwc_word, tweet_word):
	if liwc_word[-1] == "*":
		return tweet_word.startswith(liwc_word[:-1])
	else:
		return tweet_word == liwc_word

def string_contains_any(string, set):
	for item in set:
		if item in string: return True
	return False

def classify(tweet):

  pos_emoticons = [':-)', ':)', '(-:', '(:', 'B-)', ';-)', ';)', ';d', ':d']
  neg_emoticons = [':-(', ':(', ')-:', '):']

  tweet = tweet.lower()
  words = tweet.split(" ")
  word_count = len(words)
  match_count=0
  pos_count = 0
  neg_count = 0
  first_person_count=0
  second_person_count=0
  third_person_count=0
  posemo_count=0
  negemo_count=0
  cognitive_count=0
  sensory_count=0
  time_count=0
  past_count=0
  present_count=0
  future_count=0
  work_count=0
  leisure_count=0
  swear_count=0
  social_count=0
  family_count=0
  friend_count=0
  humans_count=0
  anx_count=0
  anger_count=0
  sad_count=0
  body_count=0
  health_count=0
  sex_count=0
  space_count=0
  time_count=0
  work_count=0
  achieve_count=0
  home_count=0
  money_count=0
  religion_count=0
  affect_count=0
  cause_count=0
  quant_count=0
  numb_count=0
  inhib_count=0
  ingst_count=0
  motion_count=0
  nonfl_count=0
  filler_count=0

	### look for emotions first
  emoticons_flag = 0
  if string_contains_any(tweet, pos_emoticons): emoticons_flag += 1
  if string_contains_any(tweet, neg_emoticons): emoticons_flag += 2

  if emoticons_flag == 1:
           posemo_count += 1
           match_count +=1
  if emoticons_flag == 2:
           negemo_count += 1
           match_count +=1
  #if emoticons_flag == 3: return 0

  for word in words:
    if len(word) == 0 or word[0] == '@': continue
    try:
      try:
        word = word.translate(None, string.punctuation)
      except TypeError:
        word = word.translate(string.punctuation)
    except TypeError:
      continue
    match_flag='false'
    first_flag='false'
    second_flag='false'
    third_flag='false'
    posemo_flag='false'
    negemo_flag='false'
    cognitive_flag='false'
    sensory_flag='false'
    time_flag='false'
    past_flag='false'
    present_flag='false'
    future_flag='false'
    work_flag='false'
    leisure_flag='false'
    swear_flag='false'
    social_flag='false'
    family_flag='false'
    friend_flag='false'
    humans_flag='false'
    anx_flag='false'
    anger_flag='false'
    sad_flag='false'
    body_flag='false'
    health_flag='false'
    sex_flag='false'
    space_flag='false'
    time_flag='false'
    work_flag='false'
    achieve_flag='false'
    home_flag='false'
    money_flag='false'
    religion_flag='false'
    affect_flag='false'
    cause_flag='false'
    quant_flag='false'
    numb_flag='false'
    inhib_flag='false'
    ingst_flag='false'
    motion_flag='false'
    nonfl_flag='false'
    filler_flag='false'

    for first in first_person:
      if matches(first, word):
    		first_flag='true'
    		match_flag='true'
    for second in second_person:
    	if matches(second, word):
    		second_flag='true'
    		match_flag='true'
    for third in third_person:
    	if matches(third, word):
    		third_flag='true'
    		match_flag='true'
    for pos in posemo:
    	if matches(pos, word):
    		posemo_flag='true'
    		match_flag='true'
    for neg in negemo:
    	if matches(neg, word):
    		negemo_flag='true'
    		match_flag='true'
    for cogn in cognitive:
    	if matches(cogn, word):
    		cognitive_flag='true'
    		match_flag='true'
    for sens in sensory:
    	if matches(sens, word):
    		sensory_flag='true'
    		match_flag='true'
    for t in time:
    	if matches(t, word):
    		time_flag='true'
    		match_flag='true'
    for pa in past:
    	if matches(pa, word):
    		past_flag='true'
    		match_flag='true'
    for pr in  present:
    	if matches(pr, word):
    		 present_flag='true'
    		 match_flag='true'
    for fu in future:
    	if matches(fu, word):
    		future_flag='true'
    		match_flag='true'
    for wo in work:
    	if matches(wo, word):
    		work_flag='true'
    		match_flag='true'
    for leis in leisure:
    	if matches(leis, word):
    		leisure_flag='true'
    		match_flag='true'

    for swe in swear:
    	if matches(swe, word):
    		swear_flag='true'
    		match_flag='true'

    for soc in social:
    	if matches(soc, word):
    		social_flag='true'
    		match_flag='true'
    for fam in family:
    	if matches(fam, word):
    		family_flag='true'
    		match_flag='true'
    for fri in friend:
    	if matches(fri, word):
    		friend_flag='true'
    		match_flag='true'
    for hum in humans:
    	if matches(hum, word):
    		humans_flag='true'
    		match_flag='true'
    for an in anx:
    	if matches(an, word):
    		anx_flag='true'
    		match_flag='true'
    for ang in anger:
    	if matches(ang, word):
    		anger_flag='true'
    		match_flag='true'
    for sa in sad:
    	if matches(sa, word):
    		sad_flag='true'
    		match_flag='true'
    for bo in body:
    	if matches(bo, word):
    		body_flag='true'
    		match_flag='true'
    for hea in health:
    	if matches(hea, word):
    		health_flag='true'
    		match_flag='true'
    for se in sex:
    	if matches(se, word):
    		sex_flag='true'
    		match_flag='true'
    for spa in space:
    	if matches(spa, word):
    		space_flag='true'
    		match_flag='true'
    for ti in time:
    	if matches(ti, word):
    		time_flag='true'
    		match_flag='true'
    for ach in achieve:
    	if matches(ach, word):
    		achieve_flag='true'
    		match_flag='true'
    for ho in home:
    	if matches(ho, word):
    		home_flag='true'
    		match_flag='true'
    for mo in money:
    	if matches(mo, word):
    		money_flag='true'
    		match_flag='true'
    for re in religion:
    	if matches(re, word):
    		religion_flag='true'
    		match_flag='true'
    for aff in affect:
    	if matches(aff, word):
    		affect_flag='true'
    		match_flag='true'
    for cs in cause:
    	if matches(cs, word):
    		cause_flag='true'
    		match_flag='true'
    for qt in quant:
    	if matches(qt, word):
    		quant_flag='true'
    		match_flag='true'
    for num in numb:
    	if matches(num, word):
    		numb_flag='true'
    		match_flag='true'
    for iN in inhib:
    	if matches(iN, word):
    		inhib_flag='true'
    		match_flag='true'
    for ings in ingst:
    	if matches(ings, word):
    		ingst_flag='true'
    		match_flag='true'
    for mo in motion:
    	if matches(mo, word):
    		motion_flag='true'
    		match_flag='true'
    for nonf in nonfl:
    	if matches(nonf, word):
    		nonfl_flag='true'
    		match_flag='true'
    for fill in filler:
    	if matches(fill, word):
    		filler_flag='true'
    		match_flag='true'

    if match_flag=='true':
       match_count +=1
    if first_flag=='true':
       first_person_count +=1
    if second_flag=='true':
       second_person_count +=1
    if third_flag=='true':
       third_person_count +=1
    if posemo_flag=='true':
       posemo_count +=1
    if negemo_flag=='true':
       negemo_count +=1
    if cognitive_flag=='true':
       cognitive_count +=1
    if sensory_flag=='true':
       sensory_count +=1
    if time_flag=='true':
       time_count +=1
    if past_flag=='true':
       past_count +=1
    if present_flag=='true':
       present_count +=1
    if future_flag=='true':
       future_count +=1
    if work_flag=='true':
       work_count +=1
    if leisure_flag=='true':
       leisure_count +=1
    if swear_flag=='true':
       swear_count +=1
    if social_flag=='true':
       social_count +=1
    if family_flag=='true':
       family_count +=1
    if friend_flag=='true':
       friend_count +=1
    if humans_flag=='true':
       humans_count +=1
    if anx_flag=='true':
       anx_count +=1
    if anger_flag=='true':
       anger_count +=1
    if sad_flag=='true':
       sad_count +=1
    if body_flag=='true':
       body_count +=1
    if health_flag=='true':
       health_count +=1
    if sex_flag=='true':
       sex_count +=1
    if space_flag=='true':
       space_count +=1
    if time_flag=='true':
       time_count +=1
    if achieve_flag=='true':
       achieve_count +=1
    if home_flag=='true':
       home_count +=1
    if money_flag=='true':
       money_count +=1
    if religion_flag=='true':
       religion_count +=1
    if affect_flag=='true':
       affect_count+=1
    if cause_flag=='true':
       cause_count+=1
    if quant_flag=='true':
       quant_count+=1
    if numb_flag=='true':
       numb_count+=1
    if inhib_flag=='true':
       inhib_count+=1
    if ingst_flag=='true':
       ingst_count+=1
    if motion_flag=='true':
       motion_count+=1
    if nonfl_flag=='true':
       nonfl_count+=1
    if filler_flag=='true':
       filler_count+=1
    #pos_score = pos_count/word_count
    #neg_score = neg_count/word_count

    #if pos_score > neg_score: return 1
    #if pos_score < neg_score: return -1
  return (first_person_count, second_person_count, third_person_count, posemo_count, negemo_count, cognitive_count, sensory_count, time_count, past_count, present_count, future_count, work_count,leisure_count, swear_count, social_count, family_count, friend_count, humans_count, anx_count, anger_count, sad_count, body_count, health_count, sex_count, space_count, time_count, achieve_count, home_count, money_count, religion_count,affect_count,cause_count,quant_count,numb_count,inhib_count,ingst_count,motion_count,nonfl_count,filler_count , match_count, word_count)

# --- CALLED ON IMPORT ---

cat, dic = read_liwc('LIWC2007_English080730.dic')
first_person, second_person, third_person, posemo, negemo, cognitive, sensory, time, past, present, future, work,leisure, swear, social, family, friend, humans, anx, anger, sad, body, health, sex, space, time, achieve, home, money, religion,affect,cause,quant,numb,inhib,ingst,motion,nonfl,filler= get_wordsets(dic)
