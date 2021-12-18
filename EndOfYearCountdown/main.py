from datetime import date

from deal_with_numbers import get_season, ordinal_numbers
from twitter import tweet, update_profile_image


def tweetWeeks():
    all_weeks = int((end_of_year_date - date(current_year, 1, 1)).days / 7)
    weeks_until = int(days_until / 7)
    weeks_since = ordinal_numbers(str(all_weeks - weeks_until))

    if weeks_until == 1:
        # last week, Christmas
        tweet(f"Merry Christmas! A week from now in we will be in {next_year}.", "christmas")

    elif weeks_until > 1 and weeks_until < 5:
        # last month
        tweet(f"{weeks_until} weeks left till the end of the year :calendar:", f"relaxing, animals, {season}")

    else:
        # more than five weeks left
        tweet(f"{weeks_since} week of {current_year} is starting with {weeks_until} weeks ({days_until} days) left this year. :calendar:", f"nature, animals, relaxing, {season}")

def tweetDays():
    if str(current_date) == (str(current_year) + "-01-01"):
        # first day
        tweet(f"{current_year} is finally here! I wish you all health, love, and happiness in the new year ahead. Happy New Year :tada:", "new year")
        update_profile_image(current_year)

    elif days_until == 1:
        # last day
        tweet(f"Today is the {daysBefore} day and there is only 1 day left in {current_year}! :partying_face:")

    elif days_until > 1 and days_until <= 31:
        # last month
        tweet(f"{days_until} days left till the end of the year :hourglass:", f"relaxing, animals, {season}")


current_date = date.today()
current_year = date.today().year
next_year = current_year + 1
end_of_year_date = date(next_year, 1, 1)
days_until = (end_of_year_date - current_date).days

daysBefore = current_date - date(current_year, 1, 1)
daysBefore = ordinal_numbers(str(daysBefore.days))

season = get_season(date.today().month)

if days_until % 7 == 0:
    tweetWeeks()
else:
    tweetDays()
