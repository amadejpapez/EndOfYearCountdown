from datetime import date, timedelta

from twitter import tweet, update_profile_picture


def get_season(month):
    if month in range(3, 5):
        return "spring"
    if month in range(6, 8):
        return "summer"
    if month in range(9, 11):
        return "fall"

    return "winter"


def ordinal_number(num):
    if int(num) not in range(4, 21):
        if num[-1] == "1":
            return "st"
        if num[-1] == "2":
            return "nd"
        if num[-1] == "3":
            return "rd"

    return "th"


current_day = date.today()
previous_day = current_day - timedelta(days=1)

current_year = date.today().year
next_year = current_year + 1
end_of_year_day = date(current_year, 12, 31)

days_left = (end_of_year_day - current_day).days

season = get_season(date.today().month)

if previous_day.isocalendar().week < current_day.isocalendar().week:
    weeks_all = int((end_of_year_day - date(current_year, 1, 1)).days / 7)
    week_num = current_day.isocalendar().week
    week_num_format = str(week_num) + ordinal_number(str(week_num))
    weeks_left = weeks_all - week_num

    tweet(
        f"{week_num_format} week of {current_year} is starting with {weeks_left} weeks ({days_left} days) left this year. :sun:",
        # f"{season} fun animals nature",
    )

elif current_day == date(current_year, 12, 25):
    tweet(
        f"Merry Christmas! :christmas_tree: Next week we will be in {next_year}!",
        "christmas",
    )

elif current_day == date(current_year, 12, 31):
    tweet(f"The last day of {current_year} has finally come! :partying_face:")

elif current_day == date(current_year, 1, 1):
    tweet(
        f"{current_year} is here! I wish you all health, love, and happiness in the new year. Happy New Year! :tada:",
        "new year",
    )
    update_profile_picture(current_year)
