from datetime import datetime, timedelta

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)

print("Five days ago from now was:", five_days_ago)

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday was:", yesterday)
print("Today is:", today)
print("Tomorrow will be:", tomorrow)

current_datetime = datetime.now()
dropped_microseconds = current_datetime.replace(microsecond=0)

print("Datetime with microseconds dropped:", dropped_microseconds)

date1 = datetime(2024, 2, 5, 12, 0, 0)  # First date
date2 = datetime(2024, 2, 10, 12, 0, 0)  # Second date

difference_in_seconds = (date2 - date1).total_seconds()

print("Difference between two dates in seconds:", difference_in_seconds)