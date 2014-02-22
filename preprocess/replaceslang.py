import string
from nltk.corpus import wordnet


def main():



    slang = dict()
    slangfile = open('slang.txt','rb')
    for line in slangfile:
        sl = (line.split("-")[0]).strip().lower()
        mean = (line.split("-")[1]).strip().lower()
        #print sl + mean
        slang[sl] = mean
    
    message = "wow yu seem like yu goin thru yung ladi dnt let em chang yu into that person yu gotta let go n let god!!"
    nonSlangMessage = ""

    for words in message.lower().split():
        if not wordnet.synsets(words):
            if words in slang:
                nonSlangMessage += slang[words] + " "
            else:
                nonSlangMessage += words + " "
    nonSlangMessage = nonSlangMessage[:-1]
    
    print nonSlangMessage
if __name__ == '__main__':
    main()