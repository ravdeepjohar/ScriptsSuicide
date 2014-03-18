import sys
import simplejson
import pygraphviz as pgv
import numpy as np
import networkx as nx
import pickle as pickle
from datetime import datetime
import math
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from collections import defaultdict
import matplotlib.pyplot as plt

stats = importr('stats')

deg = defaultdict(int)
indeg = defaultdict(int)
outdeg = defaultdict(int)  # seems to be the followers

fields = ["swear",   "social",  "family",  "friend",  "humans",  "affect",  "posemo",  "negemo",  "anx",     "anger",   "sad",     "cogmech", "insight", "cause",   "discrep", "tentat",  "certain", "inhib",   "incl",    "excl",    "percept", "see",    "hear",    "feel",    "bio",     "body",    "health",  "sexual",  "ingest",  "relativ", "motion",  "space",   "time",    "work",    "achieve", "leisure", "home",    "money",   "relig",   "death"] #, "calc_sentiment"]

def embed_threshold(N, i, messg_graph):
    I = N.copy()
    if messg_graph:
        for (f, t) in N.edges():
            try:
                if float(N.edge[f][t][0]['num_messages']) > 0 and float(N.edge[t][f][0]['num_messages']) > 0:
                    I.remove_edge(f,t)
                
            except KeyError:
                pass

            
    for (f, t) in I.edges():
        if len(set(N.neighbors(f)) & set(N.neighbors(t))) < i:
            I.remove_edge(f,t)
    return I

def commun_threshold(N, i):
    I = N.copy()
    if messg_graph:
        for (f, t) in N.edges():
            try:
                if float(N.edge[f][t][0]['num_messages']) > 0 and float(N.edge[t][f][0]['num_messages']) > 0:
                    I.remove_edge(f,t)
                
            except KeyError:
                pass

            
    for (f, t) in I.edges():
        if len(set(N.neighbors(f)) & set(N.neighbors(t))) < i:
            I.remove_edge(f,t)
    return I

def get_graph_stats (Is, liwc, embeds):
    mccs = list()

    plt.axis([-1, 21, -.5, .5])

    j = 0
    for i in embeds:
        I = Is[j]

        x = list()
        y = list()
        for n in I.nodes():
            if I.node[n]["from"]["messages"]["numwords"] == 0:
                x.append(0)
            else:
                x.append(I.node[n]["from"]["messages"][liwc]/I.node[n]["from"]["messages"]["numwords"])
            y.append(I.degree(n))
        xv = robjects.FloatVector(x)
        yv = robjects.FloatVector(y)
        w = stats.cor_test(xv,yv); # gives us ci
        x = [w[3][0], [w[8][0], w[8][1]]]
        mccs.append(x[0])
        line = plt.plot([i,i],x[1], [i-.2,i+.2], [x[1][0],x[1][0]], [i-.2,i+.2], [x[1][1],x[1][1]])
        plt.setp(line, 'color', 'black', 'linewidth', 2.0)
        j += 1
    mline, = plt.plot(embeds, mccs)
    plt.xlabel("Embeddedness Threshold")
    plt.ylabel("Correlation Coefficient")
    plt.title("LIWC %s vs. Degree" % liwc)
    plt.savefig("%s_deg_corr.pdf" % liwc)
    plt.close()
    plt.figure()

def plot_corrs(Is, Ms, liwc, embeds):
    print "\\begin{table}{r|r|r}"
    print "Embeddedness & Broadcast & Message\\\\"
    mccs = list()
    bccs = list()
    nmccs = list()
    nbccs = list()

    plt.axis([-1, 21, 0, .5])
    j = 0
    for i in embeds:
        I = Is[j]
        sys.stdout.write ("%d" % i)
        x = sad_corr(I, liwc)
        bccs.append(x[0])
        plt.plot([i,i],x[1])
        line = plt.plot([i,i],x[1], [i-.2,i+.2], [x[1][0],x[1][0]], [i-.2,i+.2], [x[1][1],x[1][1]])
        plt.setp(line, 'color', 'black', 'linewidth', 2.0)
        
        x = sad_messg_corr(I, liwc)
        mccs.append(x[0])
        line = plt.plot([i,i],x[1], [i-.2,i+.2], [x[1][0],x[1][0]], [i-.2,i+.2], [x[1][1],x[1][1]])
        plt.setp(line, 'color', 'black', 'linewidth', 2.0)
        j += 1
        """
        I = Ms[j]
        x = sad_corr(I, liwc)
        nbccs.append(x[0])
        plt.plot([i,i],x[1])
        line = plt.plot([i,i],x[1], [i-.2,i+.2], [x[1][0],x[1][0]], [i-.2,i+.2], [x[1][1],x[1][1]])
        plt.setp(line, 'color', 'black', 'linewidth', 2.0)

        x = sad_messg_corr(I, liwc)
        nmccs.append(x[0])
        line = plt.plot([i,i],x[1], [i-.2,i+.2], [x[1][0],x[1][0]], [i-.2,i+.2], [x[1][1],x[1][1]])
        plt.setp(line, 'color', 'black', 'linewidth', 2.0)
        """    
    bline, = plt.plot(embeds, bccs)
    mline, = plt.plot(embeds, mccs)
    #nbline, = plt.plot(embeds, nbccs)
    #nmline, = plt.plot(embeds, nmccs)
    plt.setp(bline, 'linewidth', 2.0)
    plt.setp(mline, 'linewidth', 2.0)
    #plt.setp(nmline, 'linewidth', 2.0)
    #plt.setp(nbline, 'linewidth', 2.0)
    plt.legend([bline,mline],["All messages", "Personal messages only"])
    plt.xlabel("Embeddedness Threshold")
    plt.ylabel("Assortativity")
    plt.title("LIWC %s" % liwc)

    
    plt.savefig("%s_corr.pdf" % liwc)
    plt.close()
    plt.figure()
    print "\\end{table}"
    print ("\\caption{%s}" % liwc)
                    

def sad_corr (N, liwc):
    x = list()
    y = list()
    i=0
    for (f, t) in N.edges():
        if float(N.node[f]['from']['tweets']['numwords']) == 0 or float(N.node[t]['from']['tweets']['numwords']) == 0:
            #print "yikes!: %d" % i
            i = i+1
        else:
            x.append(float(N.node[f]['from']['tweets'][liwc]) / float(N.node[f]['from']['tweets']['numwords']))
            y.append(float(N.node[t]['from']['tweets'][liwc]) / float(N.node[t]['from']['tweets']['numwords']))
            # print "Broadcast messages"
    lengthy = len(x)
    xv = robjects.FloatVector(x)
    yv = robjects.FloatVector(y)
    w = stats.cor_test(xv,yv); # gives us ci
    sys.stdout.write (" & %1.3f [%1.3f, %1.3f] & %d" %  (w[3][0], w[8][0], w[8][1], lengthy)) #cc, plus [upper,lower] ci
    return [w[3][0], [w[8][0], w[8][1]]]


def sad_messg_corr (N, liwc):
    x = list()
    y = list()
    i=0
    for (f, t) in N.edges():
        try:
            if float(N.edge[f][t][0]['num_messages']) > 0 and float(N.edge[t][f][0]['num_messages']) > 0:
                x.append(float(N.edge[f][t][0][liwc]) / float(N.edge[f][t][0]['numwords']))
                y.append(float(N.edge[t][f][0][liwc]) / float(N.edge[t][f][0]['numwords']))
        except KeyError:
            pass
            #print "Personal messages only"
            #print np.corrcoef(np.array(x),np.array(y))
    lengthy = len(x)
    xv = robjects.FloatVector(x)
    yv = robjects.FloatVector(y)
    w = stats.cor_test(xv,yv); # gives us ci
    sys.stdout.write (" & %1.3f [%1.3f, %1.3f] & %d\\\\\n" %  (w[3][0], w[8][0], w[8][1], lengthy)) #cc, plus [upper,lower] ci
    #sys.stdout.write (" & %f1.3 \\\\\n" % np.corrcoef(np.array(x),np.array(y))[1,0])
    return [w[3][0], [w[8][0], w[8][1]]]


def main ():
   
    N = nx.read_gpickle("graph/graph.pkl")
    #print "Embeddedness: 0"
    #sys.stdout.write ("0")
    #   sad_corr(N)
    #sad_messg_corr(N)
    embeds = [0,1,2,3,5,8,12,15,18,20]
    
    Is = list()
    Ms = list()
    for t in embeds:
        Is.append(embed_threshold(N,t,False))
        #Is = [embed_threshold(N, t) for t in embeds]
        #Ms.append(embed_threshold(N,t,True))
    tgraph = file("graph/threshold_graphs.pkl", "w")
    mgraph = file("graph/threshold_message_graphs.pkl", "w")

    for liwc in fields:
    #    plot_corrs(Is, Ms, liwc, embeds)


        get_graph_stats(Is, liwc, embeds)
if __name__ == "__main__":
    main()
