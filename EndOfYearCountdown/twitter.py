import os

import emoji
import requests
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


def request_images(query):
    # get 5 images from Unsplash that fit into the given query
    images = requests.get("https://api.unsplash.com/photos/random", params={"client_id": keys["PyUnsplash"]["api_key"], "count": 5, "orientation": "landscape", "query": query}).json()

    get_image(images, query)

def get_image(images, query):
    # takes image that is under 5MB, if all are over that request 5 new ones
    for img in images:
        img_data = requests.get(img["urls"]["regular"]).content

        with open(f"{DIRPATH}/photo.jpg", "wb") as myFile:
            myFile.write(img_data)

        if os.path.getsize(f"{DIRPATH}/photo.jpg") <= 5242880:
            return img["urls"]["regular"]

    request_images(query)


def tweet(text, query = None):
    if query == None:
        # tweet without an image
        api.update_status(emoji.emojize(text, use_aliases=True))
    else:
        # tweet with an image
        request_images(query)
        img_upload = api.media_upload(f"{DIRPATH}/photo.jpg")

        api.update_status(
            media_ids=[img_upload.media_id],
            status=emoji.emojize(text, use_aliases=True)
        )

def update_profile_image(current_year):
    api.update_profile_image(f"{DIRPATH}/{current_year}.jpg")
