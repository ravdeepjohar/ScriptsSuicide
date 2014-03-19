import networkx as nx
import numpy as np
import pylab as P

N = nx.read_gpickle("graph/graph.pkl")

sad = [float(N.node[name]["from"]["tweets"]["sad"])/float(N.node[name]["from"]["tweets"]["numwords"]) for name in N.nodes() if float(N.node[name]["from"]["tweets"]["numwords"])!= 0]
anx = [float(N.node[name]["from"]["tweets"]["anx"])/float(N.node[name]["from"]["tweets"]["numwords"]) for name in N.nodes() if float(N.node[name]["from"]["tweets"]["numwords"])!= 0]

n, bins, patches = P.hist(sad range=(0,1))
n, bins, patches = P.hist(anx, range=(0,1)) 
