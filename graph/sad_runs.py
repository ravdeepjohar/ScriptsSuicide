import sys
import simplejson
import pygraphviz as pgv
import networkx as nx
import numpy as np
import pylab as P
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
stats = importr('stats')



pos = [list(),list(),list()]

pos_people = [dict(), dict(), dict()]
    
def sad_runs (twitter_file):
    
    "Labels graph with Twitter data"

    tweets_json = open(twitter_file)
    while True:
        line = tweets_json.readline()
        if not line:
            break
        tweet = simplejson.loads (line)
        from_user = tweet["doc"]["from_user"]
        i = 0
        goal = "conf"
        goal = "classlabel"
        printit = False
        for name in [ "distress_result1", "distress_result2", "distress_result3" ]:
            pos[i].append(tweet["doc"][name][goal])
            if not from_user in pos_people[i]:
                pos_people[i][from_user] = list()
            pos_people[i][from_user].append(tweet["doc"][name][goal])
            if tweet["doc"][name][goal] == 1:
                printit = True
            i += 1
        
        if printit:
            sys.stdout.write (line)

    psum = [list(), list(), list()]
    i = 0
    for dic in pos_people:
        for person in dic:
            sum = 0.0
            for num in dic[person]:
                sum += num
            sum = sum / len(dic[person])
            psum[i].append(sum)
        i += 1
            
            
    n, bins, patches = P.hist(pos, range=(-1,1), bins=10,label=["1", "2", "3"], color=['crimson', 'burlywood', 'blue'])
        
    P.legend()

    P.xlabel("Distress classification")
    P.ylabel("Frequency")
    #P.title("LIWC %s" % liwc)

    
    P.savefig("graph/distress_hist.pdf")
    P.close()
    
    n, bins, patches = P.hist(psum, range=(-1,1),bins=10, label=["1", "2", "3"], color=['crimson', 'burlywood', 'blue'])
        
    P.legend()

    P.xlabel("Distress classification")
    P.ylabel("Frequency")
    #P.title("LIWC %s" % liwc)

    
    P.savefig("graph/distress_people_hist.pdf")
    P.close()

def main():
    sad_runs("data/test.json.txt")
    
if __name__ == "__main__":
    main()
