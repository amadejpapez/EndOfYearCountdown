import os
from datetime import date

import emoji
import tweepy
import wget
from PIL import Image
from pyunsplash import PyUnsplash

from auth_secrets import keys


api_key             = keys["EndOfYearCountdown"]["api_key"]
api_key_secret      = keys["EndOfYearCountdown"]["api_key_secret"]
access_token        = keys["EndOfYearCountdown"]["access_token"]
access_token_secret = keys["EndOfYearCountdown"]["access_token_secret"]

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def ordinalNumbers(number):
    if int(number) < 20:
        if number == "1": 
            number += "st"
        elif number == "2":
            number += "nd"
        elif number == "3":
            number += "rd"
        else:
            number += "th"
    else:
        tens = number[-2]
        unit = number[-1]
        if tens == "1":
           number += "th"
        else:
            if unit == "1": 
                number += "st"
            elif unit == "2":
                number += "nd"
            elif unit == "3":
                number += "rd"
            else:
                number += "th"

    global daysBefore
    daysBefore = number


def getPhoto():
    # get image from Unsplash
    unsplash = PyUnsplash(api_key=keys["PyUnsplash"]["api_key"])
    global image
    image = unsplash.photos(type_="random", count=1, featured=True, orientation="landscape", query="nature, animals, beach, see, relaxing, travel, positivity")

    if os.path.exists(f"{dirPath}/photo.jpg"):
        # remove previous "photo"
        os.remove(f"{dirPath}/photo.jpg")

    optimizePhoto()


def optimizePhoto():
    global image

    for image in image.entries:
        # download image to the current folder
        wget.download(image.link_download, out=f"{dirPath}/photo.jpg")

        if os.path.getsize(f"{dirPath}/photo.jpg") >= 3200000:
            # if image is bigger than 3.2 MB, take another one
            getPhoto()

        while os.path.getsize(f"{dirPath}/photo.jpg") >= 3072000:
            # if image is larger than 3.072 MB, optimize it as larger size will cause an error
            image = Image.open(f"{dirPath}/photo.jpg")
            image.resize((1080,566),Image.ANTIALIAS)
            image.save(f"{dirPath}/photo.jpg", quality=80)

    global haveImage
    haveImage = True



currentDate = date.today()
currentYear = date.today().year
nextYear = currentYear + 1
endOfYearDate = date(nextYear, 1, 1)
subtractDates = endOfYearDate - currentDate
daysUntil = subtractDates.days

daysBefore = currentDate - date(currentYear, 1, 1)
ordinalNumbers(str(daysBefore.days))

dirPath = os.path.dirname(os.path.realpath(__file__))

tweet = False
haveImage = False



# TWEET WEEKS if number of days is dividable by 7
if daysUntil % 7 == 0:
    weeksUntil = int(daysUntil / 7)

    if weeksUntil == 1:
        # last week of the year
        tweet = f"Only 1 week till the end of the year :calendar:"

    elif weeksUntil > 1 and weeksUntil <= 4:
        # last month
        tweet = f"Only {weeksUntil} weeks till the end of the year :calendar:"

    else:
        # when there are more than five weeks left till the end of the year
        tweet = f"There are exactly {weeksUntil} weeks left till the end of the year."


# OTHERWISE TWEET DAYS
elif str(currentDate) == (str(currentYear) + "-01-01"):
    # first day of the year
    api.update_profile_image(f"{dirPath}/{currentYear}.jpg")
    tweet = f"It’s the first day of {currentYear} and there are {daysUntil} days left until the end of the year! I wish you all health, wealth, and happiness in the new year ahead. Happy New Year! :tada:"

elif daysUntil == 1:
    # last day of the year
    tweet = f"Today is the {daysBefore} day of {currentYear} and there is only 1 day left till the end of the year! :partying_face:"

elif daysUntil > 1 and daysUntil <= 31:
    # last month
    tweet = f"Only {daysUntil} days till the end of the year :hourglass:"

elif daysUntil >= 32 and daysUntil % 5 == 0:
    # when there are more than 32 days till the end of the year
    getPhoto()
    tweet = f"Today is the {daysBefore} day of {currentYear} and there are exactly {daysUntil} days left till the end of the year. :sun:"


if tweet != False and haveImage == True:
    # if there is an image, tweet with it
    api.update_with_media(f"{dirPath}/photo.jpg", emoji.emojize(tweet, use_aliases=True))

elif tweet != False:
    # make a normal tweet
    api.update_status(emoji.emojize(tweet), use_aliases=True)