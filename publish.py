import tweepy
import os
import sys

api_key = sys.argv[1]
api_key_secret = sys.argv[2]
access_token = sys.argv[3]
access_token_secret = sys.argv[4]
status = sys.argv[5]

client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_key_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
)

tweet_content = status
client.create_tweet(text = tweet_content)