import tweepy
import config  # File with Twitter's API keys. Hidden from Version Control

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
api = tweepy.API(auth)

#api.update_status("Sending my first tweet via Tweepy!")
print(api.me().name)

