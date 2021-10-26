import os

import emoji
import tweepy
from auth_secrets import keys

api_key = keys["EndOfYearCountdown"]["api_key"]
api_key_secret = keys["EndOfYearCountdown"]["api_key_secret"]
access_token = keys["EndOfYearCountdown"]["access_token"]
access_token_secret = keys["EndOfYearCountdown"]["access_token_secret"]

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

DIRPATH = os.path.dirname(os.path.realpath(__file__))


def tweet(text):
    api.update_status(emoji.emojize(text), use_aliases=True)

def tweet_with_an_image(text):
    api.update_with_media(f"{DIRPATH}/photo.jpg", emoji.emojize(text, use_aliases=True))

def update_profile_image(current_year):
    api.update_profile_image(f"{DIRPATH}/{current_year}.jpg")
