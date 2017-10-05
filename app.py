import tweepy, csv
from conf import *

# trying one time auth
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def update_tweet(twitter_text, twitter_handle):
	if api.update_status("{} {}".format(twitter_text, twitter_handle)):
		print("Posted for: {}".format(twitter_handle))



# tweet text placeholder
twitter_text = "Welcome to #PyConfHyd"

with open("demo.csv", newline = '') as twitter_handles:
	handles = csv.reader(twitter_handles, delimiter = ',', quotechar = '"', skipinitialspace=True)	
	for twitter_handle in handles:
		for handle in twitter_handle:
			#print("{} {}".format(twitter_text, handle))
			update_tweet(twitter_text, handle)



