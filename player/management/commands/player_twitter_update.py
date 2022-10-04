from django.core.management.base import BaseCommand
from ...models import Twitter
import tweepy
from configparser import ConfigParser
import time
from selenium.common.exceptions import NoSuchElementException


class Command(BaseCommand):
    """Command class to handle function for updating player twitter attributes"""
    help = 'import data'

    def handle(self, *args, **options):
        """handle function to update twitter attributes of player"""
        configur = ConfigParser()
        configur.read('/home/sonalis/scraping/demo_scrap/scrapapp/config_folder/config.ini')

        api_key = configur.get('twitter','api_key')
        print(api_key)
        api_key_secret = configur.get('twitter','api_key_secret')

        access_token = configur.get('twitter','access_token')
        access_token_secret = configur.get('twitter','access_token_secret')

        """authentication"""
        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        for i in range(10,50):

            twitter_data = Twitter.objects.get(id=i)
            twitter_handle=twitter_data.profile_name
            try:
                """getting User timeline to get Twitter Model attributes"""
                c=api.get_user(screen_name=twitter_handle)
                print(c.screen_name, c.followers_count, c.location, c.statuses_count,c.friends_count)

                """fetching the retweet_count attribute"""
                cursor = tweepy.Cursor(api.user_timeline, screen_name=twitter_handle, tweet_mode="extended").items(1)
                retweet_count = [i.retweet_count for i in cursor]

                """fetching the last_tweet attribute"""
                statuses = api.user_timeline(screen_name=twitter_handle)
                last_tweet = str(statuses[0].text).encode('unicode_escape')
                print(last_tweet)

                """Updating Twitter Model attributes"""
                try:
                    k=Twitter.objects.filter(id=i).update(tweets_count=c.statuses_count,followers_count=c.followers_count,following_count=c.friends_count,
                                                               last_tweet=last_tweet,retweets_count=retweet_count[0],location=c.location)
                    print(k)
                except NoSuchElementException:
                    pass

            except KeyboardInterrupt as e:
                print('Status Failed On,', str(e))
                time.sleep(3)
            except Exception:
                pass

