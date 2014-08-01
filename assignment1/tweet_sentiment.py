import sys
import json
import unicodedata


def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    word_scores = {} # initialize an empty dictionary
    for line in sent_file:
  		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		word_scores[term] = int(score)  # Convert the score to an integer.
    
    tweet_file = open(sys.argv[2])
    tweet_list = []
    for line in tweet_file:
    	tweet_list.append(json.loads(line).get(u'text',0))
    
    
    answer_dict = {}
    for i in tweet_list:
    	j = tweet_list.index(i)
    	if type(i) == unicode:
    		i = str(i.encode('ascii','replace'))
    	else:
    		i = str(i)
    	
    	
    	count = 0
    	for key in word_scores:
    		if key in i:
    			count += word_scores.get(key,0)
    			answer_dict[j] = count
    		else:
    			answer_dict[j] = count
    print tweet_list[1517]
    print answer_dict[1517]
    
    
    """
   
    #hw()
    #print lines(sent_file)
    #lines(tweet_file)
    """

if __name__ == '__main__':
    main()
