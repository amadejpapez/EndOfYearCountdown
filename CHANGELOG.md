# Changelog

## [10.0] - 2022-01-31

### Changed
- remove Unsplash images as they do not add much to the tweets
- remove special tweet for the last day
- a few tweet re-wordings

## [9.0] - 2022-01-07

### Added
- tweet weeks on the actual start of the week (Monday), tweet with the number of the week, and how many weeks and days are left
- remove tweeting days every day in the last month
- remove special weeks text tweet in the last month

## [8.1] - 2022-01-06

### Changed
- images should reflect the current season
- tweeting every fifth day is removed, the bot now only tweets which week it is and how many there are till the end
- added special tweet text for Christmas

### Code
- Take API keys from a separate file
- Replace `wget` package, which has not been updated since 2015 with `requests` for image downloading
- Replace `pyunsplash` package with `requests` for sending the API request to Unsplash.com
- moved tweeting part into twitter.py

## [8.0] - 2021-06-01

### Added
- to make tweets more interesting, the bot will grab a positive nature photo from Unsplash, and add it when tweeting how many days there are till the end of the year

## [7.0] - 2021-02-13

### Added
- counts how many days passed since the new year and tweets it alongside of other data

### Changed
- changed text tweets
- removed changing bio on the first day of the year

### Code
- started using f-strings

## [6.0] - 2021-01-01

### Changed
- "only ** days left until the end of the year" will be tweeted when there are only 31 days left instead of 30
- tweet "only ** weeks left until the end of the year" in the last month
- how many days till the end of the year will be tweeted only every fifth day until the last month, instead of every tenth day

### Code
- bot now on its own determines which year is it, when does it end and which year is next, so no changes are needed when a new year starts

## [5.1] - 2021-01-01

### Changed
- tweet with "only ** days left until the end of the year" in the last month, instead of the last 20 days
- also tweet how many days until the end of the year on the first day
- updated for a new year
- changed text in bio

## [5.0] - 2020-12-26

### Changed
- when there are less than 20 days it will start tweeting with "only ** days till the end of the year"
- changed text for bio

### Code
- bot was moved to PythonAnywhere scheduled tasks
- removed `schedule` and `time` module
- added full path to the new profile image

## [4.0] - 2020-12-24

### Changed
- if there are more than 50 days till the end of the year it will only tweet every tenth day instead of tweeting every day

## [3.1] - 2020-12-12

### Added
- change profile picture on the first day of the year
- change bio to reflect a new year on the first day of the year

## [3.0] - 2020-12-02

### Changed
- changed how function calculate_weeks works, now it only tweets when there are exactly that many weeks until the end of year
- if tweeting weeks is appropriate it will tweet only tweet weeks that day, without also tweeting days
- fixed other grammar issues

### Code
- merged calculate_weeks and calculate_days functions into one endOfYearCountdown function
- merged schedule tasks from individual days all to one day

## [2.0] - 2020-02-18

### Changed
- changed text in tweets
- tweets scheduled with `schedule` module

## [1.0] - 2020-02-01
- Initial release
