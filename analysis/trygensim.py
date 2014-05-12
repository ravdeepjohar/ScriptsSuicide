import logging, gensim, bz2
from gensim import corpora, models, similarities

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

tweetfile = open("../data/tweets.txt","rb")
stoplist = open("../data/stopwords.txt", "rb")


tweets = [] 

for tweet in tweetfile:
	tweets.append(str(tweet))

#print tweets


stoplist = set(w.rstrip() for w in stoplist)


texts = [[word for word in tweet.lower().split() if word not in stoplist] 
for tweet in tweets]

# remove words that appear only once
all_tokens = sum(texts, [])
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
texts = [[word for word in text if word not in tokens_once]
          for text in texts]


dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

dictionary.save('sad_tweets.dict') 
exit()
('sad_tweets.corpus')

#lsi = gensim.models.lsimodel.LsiModel(corpus=corpus, id2word=dictionary, num_topics=400)


#print lsi.print_topics(10)
# for bla in lsi.print_topics(13):
# 	print bla


lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=10, update_every=1, chunksize=10000, passes=10)

lda.print_topics(20)


# for bla in lda.print_topics(10):
# 	print bla
# 	print " "
