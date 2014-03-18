import liwc_30categories


### read IDs
f1=open('tweets_tmp.txt','r')
myfile1=f1.read()
lines=myfile1.split('\n')
lines=lines[1:len(lines)-1]
userids=[]
tweets={}
for row in lines:
   print row
   words=row.split('\t')
   #print words[1]
   userid=str(words[0])
   tweet=str(words[2]).replace('\t',' ')

   sentiment = liwc_30categories.classify(tweet);
   print sentiment

#   userids.append(userid)
#   if userid in tweets:
#      tweets[userid]=tweets[userid]+' '+tweet
#   else: 
#      tweets[userid]=tweet
#
##f2=open('classified_twitter_30categories.tmp','a')
##line='twittername,first_person,second_person,third_person,posemo,negemo,cognitive,sensory,time,past,present,future,work,leisure, swear, social, family, friend, humans, anx, anger, sad, body, health, sex, space, time, achieve, home, money, religion, match_count,word_count'
##f2.write(line+'\n')
##f2.close()
#
#for userid in userids:
#     mystring=tweets[userid]
#     sentiment = liwc_30categories.classify(mystring);
#     line=str(userid)+','+str(sentiment[0])+','+str(sentiment[1])+','+str(sentiment[2])+','+str(sentiment[3])+','+str(sentiment[4])+','+str(sentiment[5])+','+str(sentiment[6])+','+str(sentiment[7])+','+str(sentiment[8])+','+str(sentiment[9])+','+str(sentiment[10])+','+str(sentiment[11])+','+str(sentiment[12])+','+str(sentiment[13])+','+str(sentiment[14])+','+str(sentiment[15])+','+str(sentiment[16])+','+str(sentiment[17])+','+str(sentiment[18])+','+str(sentiment[19])+','+str(sentiment[20])+','+str(sentiment[21])+','+str(sentiment[22])+','+str(sentiment[23])+','+str(sentiment[24])+','+str(sentiment[25])+','+str(sentiment[26])+','+str(sentiment[27])+','+str(sentiment[28])+','+str(sentiment[29])+','+str(sentiment[30])+','+str(sentiment[31])
#     print line
##     print
##     f2=open('classified_twitter_30categories.tmp','a')
##     f2.write(line+'\n')
##     f2.close()

f1.close()
