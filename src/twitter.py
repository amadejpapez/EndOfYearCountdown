import json
import os

import emoji
import requests
import tweepy

location = os.path.abspath(os.path.join(__file__, "../../../auth_secrets.json"))
with open(location, "r", encoding="utf-8") as myFile:
    keys = json.load(myFile)

# Migrate to Twitter API v2 when it starts supporting tweets with images
# https://trello.com/c/Zr9zDrJx/109-replacement-of-media-uploads-functionality
auth = tweepy.OAuthHandler(
    consumer_key = keys["EndOfYearCountdown"]["api_key"],
    consumer_secret = keys["EndOfYearCountdown"]["api_key_secret"]
)
auth.set_access_token(
    key = keys["EndOfYearCountdown"]["access_token"],
    secret = keys["EndOfYearCountdown"]["access_token_secret"]
)
API = tweepy.API(auth)

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
        API.update_status(emoji.emojize(text, use_aliases=True))
    else:
        # tweet with an image
        request_images(query)
        img_upload = API.media_upload(f"{DIRPATH}/photo.jpg")

        API.update_status(
            media_ids=[img_upload.media_id],
            status=emoji.emojize(text, use_aliases=True)
        )

def update_profile_image(current_year):
    API.update_profile_image(f"{DIRPATH}/{current_year}.jpg")
