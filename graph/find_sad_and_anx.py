import networkx as nx
import numpy as np
import pylab as P
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
stats = importr('stats')

sadnames = set()
anxnames = set()
def main ():
    global sadnames
    global anxnames
    N = nx.read_gpickle("graph/graph.pkl")

    sad = [float(N.node[name]["from"]["tweets"]["sad"])/float(N.node[name]["from"]["tweets"]["numwords"]) for name in N.nodes() if float(N.node[name]["from"]["tweets"]["numwords"])!= 0]
    anx = [float(N.node[name]["from"]["tweets"]["anx"])/float(N.node[name]["from"]["tweets"]["numwords"]) for name in N.nodes() if float(N.node[name]["from"]["tweets"]["numwords"])!= 0]

    n, bins, patches = P.hist([sad,anx], range=(0,1), label=["Sad", "Anxiety"], color=['crimson', 'burlywood'])
    P.legend()

    P.xlabel("Cumulative LIWC score for 1 month of Tweets")
    P.ylabel("Frequency")
    #P.title("LIWC %s" % liwc)

    
    P.savefig("graph/sad_anx_hist.pdf")
    P.close()

    sadnames = set([name for name in N.nodes() if float(N.node[name]["from"]["tweets"]["numwords"]) != 0 and float(N.node[name]["from"]["tweets"]["sad"])/float(N.node[name]["from"]["tweets"]["numwords"]) > .6])
    anxnames = set([name for name in N.nodes() if float(N.node[name]["from"]["tweets"]["numwords"]) != 0 and float(N.node[name]["from"]["tweets"]["anx"])/float(N.node[name]["from"]["tweets"]["numwords"]) > .6])

    print "# of really sad people = %d" % len(sadnames)
    print "# of really anxious people = %d" % len(anxnames)
    both = anxnames.intersection(sadnames)
    print "# of really sad AND anxious people = %d" % len(both)
    sadv = robjects.FloatVector(sad)
    anxv = robjects.FloatVector(anx)
    w = stats.cor_test(sadv, anxv)
    print "Corr coeff for sad, anx: %f" % w[3][0]


if __name__ == "__main__":
    main()

