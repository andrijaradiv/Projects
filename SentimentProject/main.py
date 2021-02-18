from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import Twitter_creds

class TwitterAuthenticator():
    
    def authenticate_twitter_app(self):
        auth = OAuthHandler(Twitter_creds.API_KEY, Twitter_creds.API_SECREPT_KEY)
        auth.set_access_token(Twitter_creds.ACCESS_TOKEN, Twitter_creds.ACCESS_TOKEN_SECRET)
        return auth

class TwitterStreamer():
    # Class for streaming and processing live tweets.
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()
    
    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authenticati
        # on and connection to the twitter streaming API.
        listener = TwitterListener(fetched_tweets_filename)     
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
        
        stream.filter(track=[hash_tag_list])

class TwitterListener(StreamListener):
    # Basic listener class that just prints recieved tweets to stout.
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
        
    def on_data(self, data):
        try:
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on data " + str(e))
        return True
    
    def on_error(self, status):
        print(status)
    
        
if __name__ == "__main__":
    hash_tag_list = ["GME", "AMC", "BB", "NOK"]
    fetched_tweets_filename = "tweets.json"
    
    twitter_streemer = TwitterStreamer()
    twitter_streemer.stream_tweets(fetched_tweets_filename, hash_tag_list)