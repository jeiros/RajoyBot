import csv
import tweepy
import config  # File with Twitter's API keys. Hidden from Version Control
from tweepy import Stream, StreamListener
import time
import random


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


def get_all_tweets(api, screen_name):
    '''Get all tweets of a user.
    Taken from https://gist.github.com/yanofsky/5436496
    Only 3240 most recent tweets'''
    all_tweets = []
    new_tweets = api.user_timeline(screen_name=screen_name,
                                   count=200,
                                   include_rts=False)
    # Don't include tweets that start with 'RT' although they shouldn't be
    # there some show up
    all_tweets.extend(
        [tweet for tweet in new_tweets if not tweet.text.startswith('RT ')])

    # save the id of the oldes tweets minus one
    oldest = all_tweets[-1].id - 1

    # keep grabbing tweets until we can't anymore
    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name=screen_name,
                                       count=200,
                                       max_id=oldest,
                                       include_rts=False)
        # Don't include tweets that start with 'RT' although they shouldn't be
        # there some show up
        all_tweets.extend(
            [tweet for tweet in new_tweets if not tweet.text.startswith('RT ')])

        oldest = all_tweets[-1].id - 1

    out_tweets = [tweet.text for tweet in all_tweets]

    return out_tweets

if __name__ == '__main__':
    api = authenticate(config)
    myStreamListener = MyStreamListener()
    myStream = Stream(auth=api.auth, listener=myStreamListener)

    while True:
        api.update_status('Random number is %d #RajoySays' %
                          random.randint(0, 1000))
        time.sleep(150)
