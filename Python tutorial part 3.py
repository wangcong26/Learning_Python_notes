# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 11:40:30 2019

@author: swang
"""

# just pass
def hello_func():
    pass

hello_func()
print(hello_func)

def hello_func():
    print('Hello Function!')
hello_func()

#DRY
def hello_func():
    return 'Hello Function!'
print(hello_func().upper())


def hello_func(greeting):
    return '{} Function.'.format(greeting)
print(hello_func('Hi'))

def hello_func(greeting, name='you'):
    return '{}, {}'.format(greeting, name)
print(hello_func('Hi', name='Corey'))

#
courses=['Math','Art']
info={'name':'John','age':22}
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
    
###############################################################################    
# use * ** to unpack list and dictionary
# without *
student_info(courses,info)
# without * **
student_info(*courses,**info)


###############################################################################





































    