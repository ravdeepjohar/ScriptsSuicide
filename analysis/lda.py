import logging, gensim, bz2
from gensim import corpora, models, similarities

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#tweetfile = open("../data/sad_tweets.txt","rb")



class MyCorpus(object):

	def __iter__(self):

		for line in open('../data/sad_tweets.txt'):
			# assume there's one document per line, tokens separated by whitespace
			yield dictionary.doc2bow(line.lower().split())

stoplist = open("../data/stopwords.txt", "rb")
	 # collect statistics about all tokens
stoplist = set(w.rstrip() for w in stoplist)

dictionary = corpora.Dictionary(line.lower().split() for line in open('../data/sad_tweets.txt'))
# remove stop words and words that appear only once
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
		 if stopword in dictionary.token2id]
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
dictionary.filter_tokens(stop_ids + once_ids) # remove stop words and words that appear only once
dictionary.compactify() # remove gaps in id sequence after words that were removed

dictionary.save('sad_tweets.dict') 
corpus_memory_friendly = MyCorpus()

tfidf = models.TfidfModel(corpus_memory_friendly)
corpus_tfidf = tfidf[corpus_memory_friendly]

lda = gensim.models.ldamodel.LdaModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=10, update_every=1, chunksize=10000, passes=100)

lda.print_topics(20)
