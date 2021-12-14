<h1 align="center">End of Year Countdown</h1>
<br>
<p align="center"><b>Twitter bot written in Python 🐍</b></p>
<p align="center"><b>Counting how many days there are till the end of the year 📆</b></p>
<p align="center"><b>Running on <a href="https://twitter.com/EndOfYearCount">@EndOfYearCount</a> since February 1, 2020</b></p>

<br>

<p align="center"><img src="images/img1_dark.jpg" width=340</p>

## 🦾 How does it work?
First, it gets the current date, month, year, and which year is next. Then it calculates how many days there are till the end of the year. If number of days can be evenly divided by 7, tweet how many full weeks there are till the end of the year.

Otherwise, it will check if tweeting days is appropriate. Over the year it tweets every fifth day, so it does not tweet too often. In the month of December it starts tweeting every day. When tweeting days it will add which day of the year is it, and a random image from [Unsplash](https://unsplash.com/). There are special tweets set for the last and the first day of the year, for Christmas and so on. On the first day of the year the bot will also update the profile picture to reflect a new year.

For communication with Twitter I am using Python library [Tweepy](https://www.tweepy.org/), and for running the bot a Tasks feature on the [PythonAnywhere](https://www.pythonanywhere.com/) website, which allows you to set how often you want to run your code.

The bot is often updated as new ideas appear.
