from datetime import date, timedelta

from twitter import tweet, update_profile_picture

def get_season(month):
    if month in range(3, 5):
        season = "spring"
    elif month in range(6, 8):
        season = "summer"
    elif month in range(9, 11):
        season = "fall"
    else:
        season = "winter"

    return season

def ordinal_number(num):
    if int(num) < 20:
        if num == "1":
            num += "st"
        elif num == "2":
            num += "nd"
        elif num == "3":
            num += "rd"
        else:
            num += "th"
    else:
        if num[-2] == "1":
            num += "th"
        else:
            unit = num[-1]
            if unit == "1":
                num += "st"
            elif unit == "2":
                num += "nd"
            elif unit == "3":
                num += "rd"
            else:
                num += "th"

    return num


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
    week_num_format = ordinal_number(str(week_num))
    weeks_left = weeks_all - week_num

    tweet(f"{week_num_format} week of {current_year} is starting with {weeks_left} weeks ({days_left} days) left this year.", f"{season} fun animals nature")

elif current_day == date(current_year, 12, 25):
    tweet(f"Merry Christmas! :christmas_tree: Next week we will be in {next_year}!", "christmas")

elif current_day == date(current_year, 12, 31):
    tweet(f"The last day of {current_year} has finally come! :partying_face:")

elif current_day == date(current_year, 1, 1):
    tweet(f"{current_year} is here! I wish you all health, love, and happiness in the new year. Happy New Year! :tada:", "new year")
    update_profile_picture(current_year)
