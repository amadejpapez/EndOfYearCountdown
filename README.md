# End of Year Countdown
**Twitter bot written in Python that tweets how many days or weeks there are till the end of the year.**

**Bot has been running on Twitter account @EndOfYearCount since February 1, 2020.**

### What does the bot do?
Bot knows which date and year is it, when does it end and which year is next. When the code is run it will determine all dates and calculate how many days there are till the end of the year. First it will check if number of days can be evenly divided by 7. If yes, it will tweet how many full weeks there are till the end of the year. If not, it will check if tweeting days is appropriate. In the beginning the bot tweeted how many days there are left every single day, now over the year it tweets every fifth day, so it does not tweet too often, until the last month, when it again starts tweeting every day. There are special tweets set for the last and the first day of the year. On the first day of the year the bot will also update the profile picture and description on Twitter to reflect a new year.

### How does it work?
Bot is written in Python and the code is often updated as new ideas appear. It uses a Python library called __Tweepy__. Tweepy is open-source on GitHub and enables communication between Python and Twitter API. You can find more about Tweepy on their [official page](https://www.tweepy.org/) or on their [GitHub repository](https://github.com/tweepy/tweepy).

This Python code is hosted on __PythonAnywhere__, which offers hosting Python code in the cloud. PythonAnywhere has a feature called Tasks, which enables you to upload your Python code and set the time when you want to run it. You can find more about PythonAnywhere on their [official page](https://www.pythonanywhere.com/).
