# IMPORT MODULES
import tweepy
import emoji
from datetime import date

# calculate how many days till the end of the year
todaysDate = date.today()
endOfYearDate = date(2022, 1, 1)
subtractDates = endOfYearDate - todaysDate
daysUntil = subtractDates.days
if(0 <= daysUntil <= 366):
    if(daysUntil >= 1 and daysUntil % 7 == 0):
        # tweet how many weeks till the end of the year if number of days is dividable by 7
        weeksUntil = daysUntil / 7
        if(weeksUntil >= 2):
            api.update_status(emoji.emojize(":date: {} weeks till the end of the year".format(int(weeksUntil)), use_aliases=True))
        else:
            # last week of the year
            api.update_status(emoji.emojize(":date: 1 week till the end of the year", use_aliases=True))
    elif(daysUntil >= 51):
        if(daysUntil % 10 == 0):
            # when there are more than 50 days till the end of the year tweet only every tenth day
            api.update_status(emoji.emojize(":clock12: {} days till the end of the year".format(daysUntil), use_aliases=True))
    elif(31 <= daysUntil <= 50):
        # when there are only 50 days till the end of the year tweet every day
        api.update_status(emoji.emojize(":clock12: {} days till the end of the year".format(daysUntil), use_aliases=True))
    elif(2 <= daysUntil <= 30):
        # when there are less than 20 days till the end of the year tweet with "only"
        api.update_status(emoji.emojize("Only {} days till the end of the year :hourglass:".format(daysUntil), use_aliases=True))
    elif(daysUntil == 1):
        # last day of the year
        api.update_status(emoji.emojize("Enjoy the last day of 2021! :smile:", use_aliases=True))
    else:
        # first day of the year
        api.update_profile_image("/home/peterindark/2022.jpg")
        api.update_profile(description=emoji.emojize("How many days or weeks till the end of 2022? :calendar:", use_aliases=True))
        api.update_status(emoji.emojize("It’s the first day of 2022! Wishing you health, wealth, and happiness in the new year ahead. Happy New Year! :tada:", use_aliases=True))
        api.update_status(emoji.emojize(":clock12: 365 days till the end of the year", use_aliases=True))
