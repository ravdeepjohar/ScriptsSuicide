import logging, gensim, bz2
from gensim import corpora, models, similarities
import pickle, re

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#tweetfile = open("../data/sad_tweets.txt","rb")

stoplist = open("../data/stopwords.txt", "rb")
     # collect statistics about all tokens
stoplist = set(w.rstrip() for w in stoplist)


def ngrams(line):

    output = ''
    line = line.lower().split()

   
    nonDotMessage = ""
    regexp = re.compile(r'\.[\.]+')

    for words in line:
        
        if regexp.search(words) is not None:
      
            nonDotMessage += re.sub(regexp, ' ', words) + " "
            
        else:
            nonDotMessage += words + " "

    line = str(nonDotMessage[:-1]).split()
   
    words = []
    for i in range(0,len(line)):
        word = line[i]
        if word in stoplist:
            pass
        else:
            words.append(line[i])

    for i in range(len(words)-2+1):
        output = output + words[i].strip() + '-' + words[i+1].strip() + " "
        
    #output = output.decode('ascii').encode('utf-8')
    
    return output

class MyCorpus(object):

    def __iter__(self):

        for line in open('random_pick.txt'):
            # assume there's one document per line, tokens separated by whitespace
            yield dictionary.doc2bow(ngrams(line).lower().split())


#print ngrams("bla bla bla lba")

#exit()

dictionary = corpora.Dictionary(ngrams(line).lower().split() for line in open('random_pick.txt'))
# remove stop words and words that appear only once


# stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
#        if stopword in dictionary.token2id]
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
dictionary.filter_tokens( once_ids ) # remove stop words and words that appear only once
dictionary.compactify() # remove gaps in id sequence after words that were removed


dictionary.save('distressed_tweets.dict') 
corpus_memory_friendly = MyCorpus()

tfidf = models.TfidfModel(corpus_memory_friendly)
corpus_tfidf = tfidf[corpus_memory_friendly]

lda = gensim.models.ldamodel.LdaModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=3, update_every=1, chunksize=10000, passes=100, alpha = 'auto')

probabilities = []
lda.print_topics()


for bla in lda.show_topics(topics = -1, topn = 20, formatted = True):
    probabilities.append(bla)

#pickle.dump(probabilities, open('prob.pickle','wb'))


#print probabilities[0]
