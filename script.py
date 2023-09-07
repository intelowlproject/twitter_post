import tweepy
import os


client = tweepy.Client(
    consumer_key=os.environ['TWITTER_API_KEY'],
    consumer_secret=os.environ['TWITTER_API_KEY_SECRET'],
    access_token=os.environ['TWITTER_ACCESS_TOKEN'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']
)


tweet_content = "Published a new release of my project! #ReleaseNotes"
client.create_tweet(text = tweet_content)