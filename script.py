import tweepy
import os

client = tweepy.Client(
    consumer_key=os.environ['api_key'],
    consumer_secret=os.environ['api_key_secret'],
    access_token=os.environ['access_token'],
    access_token_secret=os.environ['access_token_secret']
)

tweet_content = os.environ['status']
client.create_tweet(text = tweet_content)