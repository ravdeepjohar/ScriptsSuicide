import sys
import simplejson
import pygraphviz as pgv
import numpy as np
import networkx as nx
from datetime import datetime
import math
from collections import defaultdict
import liwc.categories

labels = ["first_person","second_person","third_person","posemo","negemo","cognitive","sensory","time","past","present","future","work","leisure","swear","social","family","friend","humans","anx","anger","sad","body","health","sexual","space","time","achieve","home","money","relig","Affect","cause","Quant","Numb","inhib","ingest","motion","nonfl","filler","number_classified_words","number_words"]

def main ():
         
    tweets_json = open("../data/nyc.trim.liwc")
    while True:
        d = dict()
        line = tweets_json.readline()
        if not line:
            break
        tweet = simplejson.loads (line)
       
        vals = liwc.categories.classify(tweet["doc"]["text"])
        #print len(vals)
        #print len(labels)
        for i in range(0,len(vals)):
            #print i
            d[labels[i]] = 100 * float(vals[i])/float(vals[40])
        d[labels[40]] = float(vals[40])
        for i in range(0,3):
            tweet[labels[i]] = d[labels[i]]
        print simplejson.dumps(tweet)
    

if __name__ == "__main__":
    main()
