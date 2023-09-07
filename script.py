import tweepy
import os


api_key = os.environ['TWITTER_API_KEY']
api_key_secret = os.environ['TWITTER_API_KEY_SECRET']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

# authenticating using tweepy
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# tweet content
tweet_content = "Published a new release of my project! #ReleaseNotes"

# Post the tweet
api.update_status(tweet_content)
