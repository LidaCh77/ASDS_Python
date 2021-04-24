# Create the script problem5.py,
# 1) Import datetime, time and calendar modules
# 2) Print on separate lines:
# a) Current date and time (example: 2014-09-26 16:34:40.278298)
# b) The value of the current year (example: 2014)
# c) The value of the current month (example: 9)
# d) The value of the current day of the week (example: 4 or 5 i.e. Friday)
# 3) Subtract 5 days from the current date and time and print the result (example: 2014-09-21 16:34:40.278298)
# 4) Add 5 days from the current date and time and print the result (example: 2014-10-01 16:34:40.278298)




import datetime



today = datetime.datetime.today()
print(today)
print(today.year)
print(today.month)
print(today.weekday(), 'or ', today.isoweekday())

diff_5_days = datetime.timedelta(days=5)

before_5_days = today - diff_5_days
after_5_days = today + diff_5_days

print('before_5_days : ', before_5_days)
print('after_5_days: ', after_5_days)

