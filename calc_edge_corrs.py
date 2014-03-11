import sys
import simplejson
import pygraphviz as pgv
import numpy as np
import networkx as nx
from datetime import datetime
import math
from collections import defaultdict

deg = defaultdict(int)
indeg = defaultdict(int)
outdeg = defaultdict(int)  # seems to be the followers

fields = ["swear",   "social",  "family",  "friend",  "humans",  "affect",  "posemo",  "negemo",  "anx",     "anger",   "sad",     "cogmech", "insight", "cause",   "discrep", "tentat",  "certain", "inhib",   "incl",    "excl",    "percept", "see",    "hear",    "feel",    "bio",     "body",    "health",  "sexual",  "ingest",  "relativ", "motion",  "space",   "time",    "work",    "achieve", "leisure", "home",    "money",   "relig",   "death"] #, "calc_sentiment"]

def sad_corr (N):
    x = list()
    y = list()
    i=0
    for (f, t) in N.edges():
        if float(N.node[f]['from']['tweets']['numwords']) == 0 or float(N.node[t]['from']['tweets']['numwords']) == 0:
            #print "yikes!: %d" % i
            i = i+1
        else:
            x.append(float(N.node[f]['from']['tweets']['sad']) / float(N.node[f]['from']['tweets']['numwords']))
            y.append(float(N.node[t]['from']['tweets']['sad']) / float(N.node[t]['from']['tweets']['numwords']))
    print "Broadcast messages"
    print np.corrcoef(np.array(x),np.array(y))

def sad_messg_corr (N):
    x = list()
    y = list()
    i=0
    for (f, t) in N.edges():
        try:
            if float(N.edge[f][t][0]['num_messages']) > 0 and float(N.edge[t][f][0]['num_messages']) > 0:
                x.append(float(N.edge[f][t][0]['sad']) / float(N.edge[f][t][0]['numwords']))
                y.append(float(N.edge[t][f][0]['sad']) / float(N.edge[t][f][0]['numwords']))
        except KeyError:
            pass
    print "Personal messages only"
    print np.corrcoef(np.array(x),np.array(y))

 
def main ():
   
    N = nx.read_gpickle("graph.pkl")
    print "Embeddedness: 0"
    sad_corr(N)
    sad_messg_corr(N)
    I = N.copy()
    for i in [1,5,8]:
        for (f, t) in I.edges():
            if len(set(I.neighbors(f)) & set(I.neighbors(t))) < 5:
                I.remove_edge(f,t)
        print "Embeddedness: %d" % i
        sad_corr(I)
        sad_messg_corr(I)

if __name__ == "__main__":
    main()
