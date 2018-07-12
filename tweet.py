import tweepy
import textblob
from textblob import TextBlob

consumer_key='B3eiMWFnFP2vxw2Mkee2cR4qD'
consumer_secret='PAswBztv2BQyYL9DZoSd7wmogFlU6JxWER423MPJkU5d4o8x2N'

access_token='782466154728075264-Pg2trbePRUvRIlIWtaeKZAcNhMELIll'
access_token_secret='Eypl4A0tFoY3xi5RcZg1EUiQ5G7aeOdVQL2lXwWL5wehU'

oauth=tweepy.OAuthHandler(consumer_key, consumer_secret)

oauth.set_access_token(access_token, access_token_secret)

api=tweepy.API(oauth)

public_tweets= api.search("#ENGvIND")

print(public_tweets)
