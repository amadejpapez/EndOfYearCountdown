from datetime import date

from deal_with_numbers import get_season, ordinal_numbers
from get_image import get_image
from post_on_twitter import tweet, tweet_with_an_image, update_profile_image


current_date = date.today()
current_year = date.today().year
next_year = current_year + 1
end_of_year_date = date(next_year, 1, 1)
days_until = (end_of_year_date - current_date).days

daysBefore = current_date - date(current_year, 1, 1)
daysBefore = ordinal_numbers(str(daysBefore.days))

current_month = date.today().month
season = get_season(current_month)


# TWEET WEEKS if number of days is dividable by 7
if days_until % 7 == 0:
    weeks_until = int(days_until / 7)

    if weeks_until == 1:
        # last week of the year
        tweet(f"Only 1 week till the end of the year :calendar:")

    elif weeks_until > 1 and weeks_until <= 4:
        # last month
        tweet(f"Only {weeks_until} weeks till the end of the year :calendar:")

    else:
        # when there are more than five weeks left till the end of the year
        tweet(f"There are exactly {weeks_until} weeks left till the end of the year.")


# OTHERWISE TWEET DAYS
elif str(current_date) == (str(current_year) + "-01-01"):
    # first day of the year
    update_profile_image(current_year)
    tweet(
        f"It’s the first day of {current_year} and there are {days_until} days left till the end of the year! I wish you all health, wealth, and happiness in the new year ahead. Happy New Year! :tada:"
    )

elif days_until == 1:
    # last day of the year
    tweet(
        f"Today is the {daysBefore} day of {current_year} and there is only 1 day left! :partying_face:"
    )

elif days_until > 1 and days_until <= 31:
    # last month
    tweet(f"Only {days_until} days left till the end of the year :hourglass:")

elif days_until >= 32 and days_until % 5 == 0:
    # when there are more than 32 days till the end of the year
    get_image(season)
    tweet_with_an_image(
        f"Today is the {daysBefore} day of {current_year} and there are {days_until} days left till the end of the year. :sun:"
    )
