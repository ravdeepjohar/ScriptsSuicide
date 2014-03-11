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

def initialize_graph (G):
    "Initial node and edge labels"
    
    for node in G:
        G.node[node]["to"] = dict()
        G.node[node]["to"]["messages"] = dict ()
        G.node[node]["to"]["tweets"] = dict ()
        G.node[node]["from"] = dict ()
        G.node[node]["from"]["messages"] = dict ()
        G.node[node]["from"]["tweets"] = dict ()

        G.node[node]["from"]["num_messages"] = 0 # total personal messages user sent
        G.node[node]["to"]["num_messages"] = 0   # total personal messages user received
        G.node[node]["from"]["num_tweets"] = 0   # total tweets user sent
        G.node[node]["to"]["num_tweets"] = 0     # total tweets user received
        
        G.node[node]["to"]["messages"]["numwords"] = 0
        G.node[node]["to"]["tweets"]["numwords"] = 0
        G.node[node]["from"]["messages"]["numwords"] = 0
        G.node[node]["from"]["tweets"]["numwords"] = 0
        G.node[node]["to"]["messages"]["num"] = 0
        G.node[node]["to"]["tweets"]["num"] = 0
        G.node[node]["from"]["messages"]["num"] = 0
        G.node[node]["from"]["tweets"]["num"] = 0

        for field in fields:
            G.node[node]["to"]["messages"][field] = 0
            G.node[node]["to"]["tweets"][field] = 0
            G.node[node]["from"]["messages"][field] = 0
            G.node[node]["from"]["tweets"][field] = 0
            
    
    for (u,v) in G.edges_iter():
        G.edge[u][v][0]['num_messages'] = 0 # total messages sent along edge
        G.edge[u][v][0]['numwords'] = 0  # total words
        for field in fields:
            G.edge[u][v][0][field] = 0

            
    return G

def get_graph_deg_dist(N):
    "Print degree distribution for undirected graph"
    
    indeg = defaultdict(int)
    outdeg = defaultdict(int)
    
    for n in N:
        if len(N.predecessors(n)) > 0 or len(N.predecessors(n)) > 0:
            indeg[len(N.predecessors(n))] += 1
            outdeg[len(N.successors(n))] += 1  # successors seem to be the followers

    sys.stdout.write ("Indegree distribution\n")
    sys.stdout.write (str(indeg))
    sys.stdout.write ("\nOutdegree distribution\n")
    sys.stdout.write (str(outdeg))
    sys.stdout.write ("\n\n")
    return (indeg, outdeg)

def get_recip_graph(N):
    "Returns a reciprocal graph with deg 0 nodes removed"
    
    G = N.to_undirected(reciprocal=True)

    nodeset = set()
    for n in G:
        if len(G.neighbors(n)) == 0:
            nodeset.add(n)
        
    G.remove_nodes_from(nodeset)
    return G

def label_graph (N, twitter_file):
    "Labels graph with Twitter data"

    tweets_json = open(twitter_file)
    while True:
        line = tweets_json.readline()
        if not line:
            break
        tweet = simplejson.loads (line)
        from_user = tweet["doc"]["from_user"]
        #tweet["suicidal_feelings"] = 1
        #outline = simplejson.puts(tweet)
        try:
            to_user = tweet["doc"]["to_user"]
            N.edge[to_user][from_user][0]["num_messages"] += 1  # followers graph seems to be "backwards"
            N.edge[to_user][from_user][0]["numwords"] += tweet["numwords"]  # followers graph seems to be "backward"
            N.node[to_user]["to"]["messages"]["num"] += 1
            N.node[from_user]["from"]["messages"]["num"] += 1
            N.node[to_user]["to"]["messages"]["numwords"] += tweet["numwords"]
            N.node[from_user]["from"]["messages"]["numwords"] += tweet["numwords"]
            for field in fields:
                N.edge[to_user][from_user][0][field] += float(tweet[field]) * tweet["numwords"]
                N.node[to_user]["to"]["messages"][field] += float(tweet[field]) * tweet["numwords"]
                N.node[from_user]["from"]["messages"][field] += float(tweet[field]) * tweet["numwords"]
        except KeyError:
            N.node[from_user]["from"]["tweets"]["num"] += 1
            N.node[from_user]["from"]["tweets"]["numwords"] += tweet["numwords"]
            for field in fields:
                N.node[from_user]["from"]["tweets"][field] += float(tweet[field]) * tweet["numwords"]
            for to_user in N.predecessors(from_user):
                N.node[to_user]["to"]["tweets"]["num"] += 1
                N.node[to_user]["to"]["tweets"]["numwords"] += tweet["numwords"]
                for field in fields:
                    N.node[from_user]["to"]["tweets"][field] += float(tweet[field]) * tweet["numwords"]
    return N
            
def node_to_array (node):
    "Converts node data to a numpy array"

def main ():
    G = pgv.AGraph("data/MERGED.dot", directed=True, strict=True)
    N = nx.from_agraph(G)

    sys.stdout.write ("Graph size: %d\n" % len(N))
    (indeg, outdeg) = get_graph_deg_dist(N)
    G = get_recip_graph(N)
    nx.write_gpickle(G, "recip_graph.pkl")
    sys.stdout.write ("Repicrocal graph size: %d\n" % len(G))

    for n in G:
        deg[len(G.neighbors(n))] += 1
        
    sys.stdout.write ("Degree distribution\n")
    sys.stdout.write (str(deg))
    sys.stdout.write ("\n")

    N = initialize_graph (N)
    #N = label_graph(N, "nyc.trim.append.sentiment")
    N = label_graph(N, "data/nyc.trim.liwc")
         

    nx.write_gpickle(N, "graph.pkl")

if __name__ == "__main__":
    main()
