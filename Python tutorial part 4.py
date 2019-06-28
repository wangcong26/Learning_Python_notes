# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 13:27:19 2019

@author: swang
"""



from my_module import find_index, test
import sys
# if the module we want to import is not in the current directory, then use following to append
# or we can add it to path environment
#sys.path.append('')

courses=['History','Math','Physics','CompSci']

index=find_index(courses, 'Math')
#print(index)

print(sys.path)

###############################################################################
courses=['History','Math','Physics','CompSci']
import random

random_course=random.choice(courses)
print(random_course)

###############################################################################
import math
rads=math.radians(90)
print(rads)
print(math.sin(rads))
###############################################################################
import datetime
import calendar
today=datetime.date.today()
print(today)
print(calendar.isleap(2020))
###############################################################################
import os
print(os.getcwd())
print(os.__file__) # print out the location of this file!
###############################################################################
import antigravity