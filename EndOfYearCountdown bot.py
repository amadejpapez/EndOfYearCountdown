# IMPORT MODULES
import tweepy
import emoji
from datetime import date

currentDate = date.today()
currentYear = date.today().year
nextYear = currentYear + 1
endOfYearDate = date(nextYear, 1, 1)
subtractDates = endOfYearDate - currentDate
daysUntil = subtractDates.days

# TWEET WEEKS - if number of days is dividable by 7
if(daysUntil % 7 == 0):
    weeksUntil = daysUntil / 7
    if(weeksUntil >= 5):
        api.update_status(emoji.emojize(":date: {} weeks till the end of the year".format(int(weeksUntil)), use_aliases=True))
    elif(2 <= weeksUntil <= 4):
        # in the last month of the year start tweeting weeks with "only"
        api.update_status(emoji.emojize("Only {} weeks left till the end of the year :hourglass:".format(int(weeksUntil)), use_aliases=True))
    elif(weeksUntil == 1):
        # last week of the year
        api.update_status(emoji.emojize("Only 1 week left till the end of the year :hourglass:", use_aliases=True))
# OTHERWISE TWEET DAYS
elif(str(currentDate) == str(currentYear) + "-01-01"):
    # first day of the year
    api.update_profile_image("/home/**/{}.jpg".format(currentYear))
    api.update_profile(description=emoji.emojize("How many days or weeks till the end of {}? :calendar:".format(currentYear), use_aliases=True))
    api.update_status(emoji.emojize("It’s the first day of {}! Wishing you health, wealth, and happiness in the new year ahead. Happy New Year! :tada:".format(currentYear), use_aliases=True))
    api.update_status(emoji.emojize(":clock12: {} days till the end of the year".format(daysUntil), use_aliases=True))
elif(daysUntil >= 32 and daysUntil % 5 == 0):
    # when there are more than 50 days till the end of the year tweet only every fifth day
    api.update_status(emoji.emojize(":clock12: {} days till the end of the year".format(daysUntil), use_aliases=True))
elif(2 <= daysUntil <= 31):
    # in the last month start tweeting with "only"
    api.update_status(emoji.emojize("Only {} days left till the end of the year :hourglass:".format(daysUntil), use_aliases=True))
elif(daysUntil == 1):
    # last day of the year
    api.update_status(emoji.emojize("Enjoy the last day of {} :smile:".format(currentYear), use_aliases=True))
