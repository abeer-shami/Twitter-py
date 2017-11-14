import tweepy
from textblob import TextBlob

consumer_key= '2v6nkOKXqUG7mAUKMDOXkkrey'
consumer_secret= '5NswPby3STpD7PpODiBrPSRGlqFhOCKgGq0Vwj72CpUzWbQDiE'

access_token='929752297340534786-pXd0olkpF6dBDfDK5mL2oY9j5ugKPUU'
access_token_secret='HemetwwLBwamM6pt4CWgk2IV2TtUfuGEnS40U7v9jiMyt'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Syria')


for tweet in public_tweets:
    print(tweet.text)

    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")