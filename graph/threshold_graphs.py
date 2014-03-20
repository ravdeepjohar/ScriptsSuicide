import networkx as nx
import pickle as pickle


def main ():
   
    N = nx.read_gpickle("graph/graph.pkl")

    G = N.to_undirected(reciprocal=True)
    H = nx.graph()

    for u,v in G.edges_iter():
    	if not H.has_edge(u,v):
	   H.add_edge(u,v)

    c = nx.communicability(H)

    pickle.dump(c, "communicability_H.pkl")
    nx.write_gpickle(H, "graphH.pkl")

if __name__ == "__main__":
    main()
