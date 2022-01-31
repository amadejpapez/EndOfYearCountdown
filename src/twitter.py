"""
Handles posting to Twitter.

API keys are stored in a separate 'auth_secrets.json' file.
It is located outside of the EndOfYearCountdown project folder.

File structure:
-----------------------------
{
    "EndOfYearCountdown" : {
        "api_key"               : "x",
        "api_key_secret"        : "x",
        "access_token"          : "x",
        "access_token_secret"   : "x"
    }
}
-----------------------------
"""

import json
import os

import emoji
import tweepy

AUTH_LOC = os.path.abspath(os.path.join(__file__, "../../../auth_secrets.json"))
with open(AUTH_LOC, "r", encoding="utf-8") as authFile:
    KEYS = json.load(authFile)

API = tweepy.Client(
    consumer_key=KEYS["EndOfYearCountdown"]["api_key"],
    consumer_secret=KEYS["EndOfYearCountdown"]["api_key_secret"],
    access_token=KEYS["EndOfYearCountdown"]["access_token"],
    access_token_secret=KEYS["EndOfYearCountdown"]["access_token_secret"]
)

DIRPATH = os.path.dirname(os.path.realpath(__file__))


def tweet(text):
    API.create_tweet(
        text=emoji.emojize(text, use_aliases=True),
    )
