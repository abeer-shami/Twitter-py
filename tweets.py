# import tweepy
# from textblob import TextBlob

# consumer_key= '2v6nkOKXqUG7mAUKMDOXkkrey'
# consumer_secret= '5NswPby3STpD7PpODiBrPSRGlqFhOCKgGq0Vwj72CpUzWbQDiE'

# access_token='929752297340534786-pXd0olkpF6dBDfDK5mL2oY9j5ugKPUU'
# access_token_secret='HemetwwLBwamM6pt4CWgk2IV2TtUfuGEnS40U7v9jiMyt'

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

# public_tweets = api.search('Syria')


# for tweet in public_tweets:
#     print(tweet.text)

#     analysis = TextBlob(tweet.text)
#     print(analysis.sentiment)
#     print("")

#the third way to getting the tweets it's work and saving in csv file but the if statment didn't work with me
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time


'''  
 trying to connect the db    
# con = mariadb.connect("http://127.0.0.1:5000","tweet","tweet")

# c = con.cursor()
'''
ckey= '2v6nkOKXqUG7mAUKMDOXkkrey'
csecret= '5NswPby3STpD7PpODiBrPSRGlqFhOCKgGq0Vwj72CpUzWbQDiE'
atoken= '929752297340534786-pXd0olkpF6dBDfDK5mL2oY9j5ugKPUU'
asecret= 'HemetwwLBwamM6pt4CWgk2IV2TtUfuGEnS40U7v9jiMyt'
class listener(StreamListener):
    def on_data(self, data):
        try:
            #print data
            tweet = data.split(',"text":"')[1].split('","source')[0]
            print tweet

            saveThis = str(time.time())+'::'+tweet
            saveFile = open('tweety.csv','a')
            saveFile.write(saveThis)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException, e:
            print 'failed ondata, ',str(e)
            time.sleep(5)
            
    
    def on_error(self, status):
        print status


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream=Stream(auth,listener())
twitterStream.filter(track=["Syria"])