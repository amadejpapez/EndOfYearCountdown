# IMPORT MODULES
# if you see an error you need to first install them
import tweepy
import emoji
import schedule
import time
from datetime import date


# CALCULATE DAYS UNTIL 2021
def calculate_days():
    date1 = date.today()
    date2 = date(2021, 1, 1)
    days_until = date2 - date1
    api.update_status(emoji.emojize(":clock12: {} days till the end of year".format(days_until.days), use_aliases=True))

schedule.every().monday.at("06:00").do(calculate_days)
schedule.every().tuesday.at("06:00").do(calculate_days)
schedule.every().wednesday.at("06:00").do(calculate_days)
schedule.every().thursday.at("06:00").do(calculate_days)
schedule.every().friday.at("06:00").do(calculate_days)
schedule.every().saturday.at("06:00").do(calculate_days)
schedule.every().sunday.at("06:00").do(calculate_days)

while True:
    schedule.run_pending()
    time.sleep(1)


# CALCULATE WEEKS UNTIL 2021
def calculate_weeks():
    date1 = date.today()
    date2 = date(2021, 1, 1)
    days_until = date2 - date1
    weeks_until = days_until.days // 7 
    api.update_status(emoji.emojize(":date: {} weeks till the end of year".format(weeks_until), use_aliases=True))

schedule.every().sunday.at("06:15").do(calculate_weeks)

while True:
    schedule.run_pending()
    time.sleep(1)
