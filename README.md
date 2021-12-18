<h1 align="center">End of Year Countdown</h1>
<br>
<p align="center"><b>Twitter bot written in Python 🐍</b></p>
<p align="center"><b>Counting how many days there are till the end of the year 📆</b></p>
<p align="center"><b>Running on <a href="https://twitter.com/EndOfYearCount">@EndOfYearCount</a> since February 1, 2020</b></p>

<br>

<p align="center"><img src="images/img1_dark.jpg" width=340</p>

## 🦾 How does it work?
First, it gets the current date, month, year, and which year is next. Then it calculates how many days there are till the end of the year. If number of days are divided by 7 and the remainder is 0, tweet which week of the year is it and how many days and weeks there are till the end of the year.

Otherwise, it will check tweeting days. There are special tweets set for the last day, New Year and Christmas. On the first day of the year the bot will update the profile picture to reflect a new year.

Most tweets now contain a random image from [Unsplash](https://unsplash.com/) to make them more interesting.

For communication with Twitter I am using Python library [Tweepy](https://www.tweepy.org/), and for running the bot a Tasks feature on the [PythonAnywhere](https://www.pythonanywhere.com/) website, which allows you to set how often you want to run your code.

The bot is often updated as new ideas appear.
