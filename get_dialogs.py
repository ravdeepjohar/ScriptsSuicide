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

def get_recip_graph(N):
    "Returns a reciprocal graph with deg 0 nodes removed"
    
    G = N.to_undirected(reciprocal=True)

    nodeset = set()
    for n in G:
        if len(G.neighbors(n)) == 0:
            nodeset.add(n)
        
    G.remove_nodes_from(nodeset)
    return G

def label_graph (U, twitter_file, G):
    tweets_json = open(twitter_file)

    while (True):
        line = tweets_json.readline()
        if not line:
            break
        tweet = simplejson.loads (line)
        from_user = tweet["doc"]["from_user"]
        try:
            to_user = tweet["doc"]["to_user"]
            if G.edge[to_user][from_user][0]["num_messages"] >= 10 and G.edge[from_user][to_user][0]["num_messages"] >= 10:
                (one, two) = sorted((to_user, from_user))
                if not "tweets" in U.edge[one][two][0]:
                    U.edge[one][two][0]["tweets"] = list()
                U.edge[one][two][0]["tweets"].append(tweet)
        except KeyError:
            pass
    for n,nbrs in U.adjacency_iter():
        for nbr,eattr in nbrs.items():
            if "tweets" in eattr[0]:
                for tweet in eattr[0]["tweets"]:
                    print "%s %s %s %s %s" % (tweet["doc"]["from_user"], tweet["doc"]["to_user"], tweet["doc"]["created_at"], tweet["doc"]["text"].encode("utf-8"), tweet["posemo"], tweet["negemo"])
                    
         

G = nx.read_gpickle("graph.old.pkl")

U = get_recip_graph(G)


label_graph(U, "nyc.trim.liwc", G)
