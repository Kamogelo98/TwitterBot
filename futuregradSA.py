# import packages
import pip
import tweepy
import time


#Authenticate to twitter


consumer_key = 'rKFmWSa01fnMjz50KaqJYex7u'
consumer_secret = 'LnUUCsDSDxfdohPU5fGKUdwUAOwfWunJ0PGB1UBuTK8qpgiPqg'
access_key = '1416120000746819585-EvimEUhvtiZBA7doAUWrvy5lCaR5oZ'
access_secret = 'lDNGX1SUvbCxJnI8nPzudoxhNThiuBejVsBdAaZrnAhcP'

#Create API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_acess_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limitc=True, wait_on_rate_limit_notify=True)


user = api.me()
search= 'universityStudyTips'
num_of_tweets = 1000

for tweet in tweepy.Cursur(api.search, search).items(num_of_tweets):
    try:

        tweet.retweet()
        print("Retweet")
        time.sleep(0)
    except tweepy.TweepError as e:
            print(e.reason)
    except StopIteration:
                break