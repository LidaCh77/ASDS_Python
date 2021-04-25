# Create the script ​problem4.py, 

# ​which gets 2 optional command line arguments num_y​ (the number of years) of type int and ​num_d​ (the number of days) of type int. Print current date and time + ​num_y +​ ​num_d ​(using the timedelta function), taking into consideration that both of the variables are optional and if one or both are not given by the user they shouldn’t be included in the resulting sum.

# Example of the output:
    
# “Current date: 2019-08-17 13:57:28.13050” 
# “Given years: 2”
# “Given days: not given”
# “Final date: 2021-08-17 13:57:28.13050”





import argparse
import datetime


parser = argparse.ArgumentParser()

parser.add_argument('--num_y', help = 'number of year', type = int)
parser.add_argument('--num_d', help = 'number of days', type = int)

args = parser.parse_args()

current_date = datetime.datetime.today()


print('Current date: ', current_date)

if args.num_y & args.num_d:
    diff_year = datetime.timedelta(days = 365*args.num_y)
    diff_day = datetime.timedelta(days = args.num_d)
    print('Given years: ', args.num_y)
    print('Given days: ', args.num_d)
    print('Final date: ', current_date + diff_year + diff_day) 
elif not args.num_y & args.num_d:
    diff_day = datetime.timedelta(days = args.num_d)
    print('Given years: ','not given')
    print('Given days: ', args.num_d)
    print('Final date: ', current_date + diff_day)      
elif not args.num_d & args.num_y:
    diff_year = datetime.timedelta(days = 365*args.num_y)
    print('Given days: ','not given')    
    print('Given year: ',args.num_y)
    print('Final date: ', current_date + diff_year)      
else:
    print('Given years: ','not given')     
    print('Given days: ','not given')  
    print('Final date: ', current_date)











