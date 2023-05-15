import tweepy
import os
from dotenv import load_dotenv

load_dotenv()


class TwitterUtils:
    def __init__(self):
        self.api_key = os.getenv("api_key")
        self.api_secret = os.getenv("api_secret")
        self.access_token = os.getenv("access_token")
        self.access_token_secret = os.getenv("access_token_secret")
        self.api = self.twitter_api()

    def twitter_api(self):

        auth = tweepy.OAuthHandler(self.api_key, self.api_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        try:
            api.verify_credentials()
        except Exception as e:
            print("Error creating API")
            raise e
        print("API created")
        return api

    def tweet(self, status: str, filename=None, tweet_id=None):
        try:
            if filename:
                media = self.api.media_upload(filename)
                tweet_info = self.api.update_status(
                    status=status, media_ids=[media.media_id], in_reply_to_status_id=tweet_id
                )
            else:
                tweet_info = self.api.update_status(status=status, in_reply_to_status_id=tweet_id)
            print("Tweet successfully sent")
            return tweet_info
        except tweepy.TweepyException as e:
            print(e)