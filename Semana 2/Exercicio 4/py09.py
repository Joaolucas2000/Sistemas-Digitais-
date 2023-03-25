#Python Tutorial for Beginners 9: Import Modules and Exploring The Standard Library


import sys 
sys.path.append('/home/MyModules')

from my_module import find_index, test

courses = ['History','Math','Physics', 'CompSci']

index = find_index(courses, 'Math')
print(sys.path)
                


import math 

rads = math.radians(90)
print(math.sin(rads))


import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap())
