#1
import time
import calendar
import datetime

#2

my_bday = datetime.date(1994,9,18)
print('My Birthday: ',my_bday) 
print('The Year of My Birthday: ',my_bday.year) 
print('The Month of My Birthday: ',my_bday.month) 
print('The Day of My Birthday: ',my_bday.day) 
print('The Weekday of My Birthday: ',my_bday.isoweekday()) 
upcoming_bday = datetime.date(2021,9,18)
today = datetime.date.today()
diff =  upcoming_bday - today
print('Day are left till my upcoming birthday: ', diff)



#3

may_2017 = calendar.month(2017,5)
print('Here is the calendar of May 2017')
print(may_2017) 


#4

delta_1 = datetime.timedelta(days=1)
delta_2 = datetime.timedelta(days=2)
delta_3 = datetime.timedelta(days=3)
yesterday = datetime.datetime.today() - delta_1
print('Yesterday date and time:', yesterday) 
add_2 = yesterday + delta_2
print('Added 2 days: ', add_2) 

before_3 = yesterday - delta_3
print('Subtracted 3 days: ', before_3) 

































