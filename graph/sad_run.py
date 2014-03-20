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
        goal = "classlabel"
        if tweet["doc"]["distress_result3"][goal] == 1:
            sys.stdout.write (line)


def main():
    sad_runs("data/test.json.txt")
    
if __name__ == "__main__":
    main()
