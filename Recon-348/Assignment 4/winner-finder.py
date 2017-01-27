def keywords(filepath):
	keywords = []
	wordfile = open(filepath, "r")
	for line in wordfile:
		keywords.append(line)
	return keywords

def useful_filter(search_array, data, or_flag=True):
	matchingLines = []
	while(search_array):
		search_elt = search_array.pop()
		elt_matchingLines = filter (lambda (line):
			(search_elt.lower() in line.lower()), data)
		if(or_flag):
			matchingLines = list(set(elt_matchingLines+matchingLines))
		else:
			matchingLines = list(set(elt_matchingLines) & set(matchingLines))
	return matchingLines
		

GG_tweet_id = "18667907"

keywords = keywords("keywords.txt")

tweets = list(open("goldenglobes.tab","r"))

GG_tweets = useful_filter([GG_tweet_id], tweets)

awards = useful_filter(["congratulations"], GG_tweets)

host_GG_tweets = useful_filter(["host"], GG_tweets)
presenter_GG_tweets = useful_filter(["present"], GG_tweets)

execfile("bayesBestOld.py")

def opinion_score(term, tweets = tweets):
        term_tweets = useful_filter([term], tweets)
        good_score = 0
        bad_score = 0
        for tweet in term_tweets:
                classification = myBayes.classify(tweet.split("\t")[0])
                if classification == 'positive':
                        good_score += 1
                elif classification == 'negative':
                        bad_score += 1
        return (good_score, bad_score)

print opinion_score("Meryl Streep")
print opinion_score("Tom Hanks")
print opinion_score("Jimmy Fallon")
