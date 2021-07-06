def ordinal_numbers(num):
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
