<h1 align="center">End of Year Countdown</h1>
<br>
<p align="center"><b>Twitter bot written in Python 🐍</b></p>
<p align="center"><b>Counting how many days and weeks there are left this year 📆</b></p>

<br>

<p align="center"><b>Was running on a Twitter account <i>@EndOfYearCount</i>
<br>
from February 1, 2020 to September 18, 2022</b></p>

<br>

<p align="center"><img src="images/twitter_profile.jpeg" width=340</p>

<br>

## 🦾 How does it work?

It gets info like current date, month, year, which year is next and so on. Then it calculates how many days and weeks there are till the end of the year.

If current day is Monday, start of a week, it will make a tweet which week number is starting and how many days and weeks there are left this year.

Special tweets are set for New Year and Christmas. There were more tweets but were removed, so the bot did not tweet too often.

For communication with Twitter I am using a Python library [Tweepy](https://github.com/tweepy/tweepy), and for running the bot daily, a Scheduled Tasks feature on [PythonAnywhere](https://www.pythonanywhere.com/).
