import tweepy
import emoji
from datetime import date

api_key = "x"
api_secret_key = "x"
access_token = "x"
access_secret_key = "x"

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_secret_key)
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


currentDate = date.today()
currentYear = date.today().year
nextYear = currentYear + 1
endOfYearDate = date(nextYear, 1, 1)
subtractDates = endOfYearDate - currentDate
daysUntil = subtractDates.days

daysBefore = currentDate - date(currentYear, 1, 1)
ordinalNumbers(str(daysBefore.days))


# TWEET WEEKS if number of days is dividable by 7
if daysUntil % 7 == 0:
    weeksUntil = int(daysUntil / 7)

    if weeksUntil == 1:
        # last week of the year
        api.update_status(emoji.emojize(f"Only 1 week till the end of the year :calendar:", use_aliases=True))

    elif weeksUntil > 1 and weeksUntil <= 4:
        # last month
        api.update_status(emoji.emojize(f"Only {weeksUntil} weeks till the end of the year :calendar:", use_aliases=True))

    else:
        # when there are more than five weeks left till the end of the year
        api.update_status(f"There are exactly {weeksUntil} weeks left till the end of the year.")

# OTHERWISE TWEET DAYS
elif str(currentDate) == str(currentYear) + "-01-01":
    # first day of the year
    api.update_profile_image(f"/home/x/{currentYear}.jpg")
    api.update_status(emoji.emojize(f"It’s the first day of {currentYear} and there are {daysUntil} days left until the end of the year! I wish you all health, wealth, and happiness in the new year ahead. Happy New Year! :tada:", use_aliases=True))

elif daysUntil == 1:
    # last day of the year
    api.update_status(emoji.emojize(f"Today is the {daysBefore} day of {currentYear} and there is only 1 day left till the end of the year! :partying_face:", use_aliases=True))

elif daysUntil > 1 and daysUntil <= 31:
    # last month
    api.update_status(emoji.emojize(f"Only {daysUntil} days till the end of the year :hourglass:", use_aliases=True))

elif daysUntil >= 32 and daysUntil % 5 == 0:
    # when there are more than 32 days till the end of the year
    api.update_status(f"Today is the {daysBefore} day of {currentYear} and there are {daysUntil} days left till the end of the year.")