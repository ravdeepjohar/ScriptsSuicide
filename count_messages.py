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


         

G = nx.read_gpickle("graph.pkl")
for n,nbrs in G.adjacency_iter():
    for nbr,eattr in nbrs.items():
        if (eattr[0]["num_messages"]) > 0:
            print "%s %s %d" % (n, nbr, eattr[0]["num_messages"])
          


