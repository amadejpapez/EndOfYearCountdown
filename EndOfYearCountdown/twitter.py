import os

import emoji
import requests
import tweepy
from auth_secrets import keys
from pyunsplash import PyUnsplash

api_key = keys["EndOfYearCountdown"]["api_key"]
api_key_secret = keys["EndOfYearCountdown"]["api_key_secret"]
access_token = keys["EndOfYearCountdown"]["access_token"]
access_token_secret = keys["EndOfYearCountdown"]["access_token_secret"]

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

DIRPATH = os.path.dirname(os.path.realpath(__file__))


def get_image(season):
    # request image from Unsplash
    unsplash = PyUnsplash(api_key=keys["PyUnsplash"]["api_key"])
    image = unsplash.photos(
        type_="random",
        count=1,
        featured=True,
        orientation="landscape",
        query=season,
    )

    check_image(image, season)

def check_image(image, season):
    for image in image.entries:
        # download image to the current folder
        img_data = requests.get(image.link_download).content

        with open(f"{DIRPATH}/photo.jpg", "wb") as myFile:
            myFile.write(img_data)
        
    if os.path.getsize(f"{DIRPATH}/photo.jpg") >= 5242880:
        get_image(season)


def tweet(text, season = None):
    if season == None:
        # tweet without an image
        api.update_status(emoji.emojize(text, use_aliases=True))
    else:
        # tweet with an image
        get_image(season)
        img_upload = api.media_upload(f"{DIRPATH}/photo.jpg")

        api.update_status(
            media_ids=[img_upload.media_id],
            status=emoji.emojize(text, use_aliases=True)
        )

def update_profile_image(current_year):
    api.update_profile_image(f"{DIRPATH}/{current_year}.jpg")
