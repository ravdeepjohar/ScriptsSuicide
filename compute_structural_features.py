import sys
import simplejson
import pygraphviz as pgv
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime
import math
from collections import defaultdict

deg = defaultdict(int)
indeg = defaultdict(int)
outdeg = defaultdict(int)  # seems to be the followers

fields = ["swear",   "social",  "family",  "friend",  "humans",  "affect",  "posemo",  "negemo",  "anx",     "anger",   "sad",     "cogmech", "insight", "cause",   "discrep", "tentat",  "certain", "inhib",   "incl",    "excl",    "percept", "see",    "hear",    "feel",    "bio",     "body",    "health",  "sexual",  "ingest",  "relativ", "motion",  "space",   "time",    "work",    "achieve", "leisure", "home",    "money",   "relig",   "death", "calc_sentiment"]

class GraphData:
    cc = list()

GD = GraphData()
ND = GraphData()

def main ():
    

    ND.cc = nx.strongly_connected_components(N)
    plt.barh(range(0,44), [len(g) for g in ND.cc][0:44])
    plt.savefig("sccs.pdf")

    GD.cc = nx.connected_components(G)
    plt.barh(range(0,len(GD.cc)), [len(g) for g in GD.cc])
    plt.savefig("ccs.pdf")

    

    

if __name__ == "__main__":
    N = nx.read_gpickle("graph.pkl")
    G = nx.read_gpickle("recip_graph.pkl")
    main()
