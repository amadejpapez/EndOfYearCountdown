# IMPORT MODULES
import tweepy
import emoji
import schedule
import time
from datetime import date


# END OF YEAR COUNTDOWN BOT
def endOfYearCountdown():
    # calculate how many days till the end of the year
    todaysDate = date.today()
    endOfYearDate = date(2021, 1, 1)
    subtractDates = endOfYearDate - todaysDate
    daysUntil = subtractDates.days
    # check if the bot should tweet how many weeks till the end of the year and tweet that if appropriate
    if(daysUntil % 7 == 0):
        # calculate how many weeks till the end of the year
        weeksUntil = daysUntil / 7
        if(weeksUntil > 1):
            api.update_status(emoji.emojize(":date: {} weeks till the end of the year".format(int(weeksUntil)), use_aliases=True))
        if(weeksUntil == 1):
            # if it's the last week of the year
            api.update_status(emoji.emojize(":date: 1 week till the end of the year", use_aliases=True))
    if(daysUntil % 7 != 0):
        # if tweeting weeks is not appropriate tweet how many days till the end of the year
        if(daysUntil > 1):
            api.update_status(emoji.emojize(":clock12: {} days till the end of the year".format(daysUntil), use_aliases=True))
        if(daysUntil == 1):
            # if it's the last day of the year
            api.update_status(emoji.emojize("Enjoy your last day of the year! :grinning:", use_aliases=True))
    if(daysUntil == 0):
        # if it's the first day of the year
        api.update_profile_image("2021.jpg")
        api.update_profile(description=emoji.emojize("How many days or weeks till the end of 2021? | new tweet every day :robot:", use_aliases=True))
        api.update_status(emoji.emojize("It’s the first day of 2021! Wishing you health, wealth, and happiness in the new year ahead. Happy New Year! :tada:", use_aliases=True))

schedule.every().day.at("06:00").do(endOfYearCountdown)

while True:
    schedule.run_pending()
    time.sleep(1)
