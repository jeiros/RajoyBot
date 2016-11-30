import tweepy
import config  # File with Twitter's API keys. Hidden from Version Control
from tweepy import Stream, StreamListener


class MyStreamListener(StreamListener):

    """docstring for Listener"""

    def on_status(self):
        print(status.text)

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print(status)

def authenticate(config):
    'Authenticate with OAuth'
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
    return tweepy.API(auth)

if __name__ == '__main__':
    api = authenticate(config)
    myStreamListener = MyStreamListener()
    myStream = Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=['Rajoy'])
