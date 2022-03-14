import os
from datetime import date, timedelta
from json import load

import tweepy
from emoji import emojize


def tweet(tweet_text):
    """Send a tweet to Twitter via API v2"""

    LOC = os.path.abspath(os.path.join(__file__, "../../../auth_secrets.json"))
    with open(LOC, "r", encoding="utf-8") as auth_file:
        KEYS = load(auth_file)

    API = tweepy.Client(
        consumer_key=KEYS["EndOfYearCountdown"]["api_key"],
        consumer_secret=KEYS["EndOfYearCountdown"]["api_key_secret"],
        access_token=KEYS["EndOfYearCountdown"]["access_token"],
        access_token_secret=KEYS["EndOfYearCountdown"]["access_token_secret"],
    )

    API.create_tweet(text=emojize(tweet_text, language="alias"))


def ordinal_number(num):
    """Add an ordinal number suffix to numbers."""
    if int(num) not in range(4, 21):
        if num[-1] == "1":
            return "st"
        if num[-1] == "2":
            return "nd"
        if num[-1] == "3":
            return "rd"

    return "th"


def format_tweet(current_date):
    """
    Does the checking if tweeting is needed for today.
    If not, it returns None. Otherwise a formatted tweet.

    ---
    5th week of 2022 is starting with 47 weeks (334 days) left this year. ☀️
    ---
    """

    current_year = date.today().year
    end_of_year_day = date(current_year, 12, 31)

    yesterday_date = current_date - timedelta(days=1)
    days_left = (end_of_year_day - current_date).days

    if yesterday_date.isocalendar().week < current_date.isocalendar().week:
        all_weeks = int((end_of_year_day - date(current_year, 1, 1)).days / 7)
        week_num = current_date.isocalendar().week
        week_num_format = str(week_num) + ordinal_number(str(week_num))
        weeks_left = all_weeks - week_num

        return f"{week_num_format} week of {current_year} is starting with {weeks_left} weeks ({days_left} days) left. :sun:"

    if current_date == date(current_year, 12, 25):
        return f"Merry Christmas!:christmas_tree: Don't forget that there are only {days_left} days left this year!"

    if current_date == date(current_year, 1, 1):
        return f"I wish you all health, love, and happiness in {current_year}. Happy New Year! :tada:"

    return None


text = format_tweet(date.today())
if text:
    tweet(text)
