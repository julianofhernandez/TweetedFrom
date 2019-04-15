import tweepy
auth = tweepy.OAuthHandler("Consumer API Key", "Consumer API Key Secret")
auth.set_access_token("Access Token", "Access Token Secret")
api = tweepy.API(auth)
print ("Tweet from terminal")
print ("Tweeted from ...")
tweet = raw_input("What Would You Like To Tweet? ")
api.update_status(tweet)
print ("Done!")
