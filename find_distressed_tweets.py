import re
import simplejson

def main ():
    tweet_file = open ("data/nyc.trim.liwc")
    annotations_chris = open("250completed_dataset_Cissi.txt")
    lines = annotations_chris.readlines()
    codes = dict()
    for line in lines:
        m = re.search('(?<=Msg_id: )([0-9]+)\s+\[\S+:\s+(\S*),\s*(\S.*):\s*(\S*)\s*\]', line)
        if m:
            codes[int(m.group(1))] = [m.group(2), m.group(3), m.group(4)]
    while True:
        line = tweet_file.readline()
        if not line:
            break
        tweet = simplejson.loads (line)
        id = tweet["doc"]["id"]
        if id in codes:
            tweet["distress"] = codes[id][0]
            tweet["category"] = codes[id][1]
            tweet["in_category"] = codes[id][2]
            print simplejson.dumps(tweet)
            
if __name__ == "__main__":
    main()

