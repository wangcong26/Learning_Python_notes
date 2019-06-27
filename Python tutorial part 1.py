# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 13:08:10 2019
https://www.youtube.com/watch?v=k9TUPpGqYTo
@author: swang
"""
##1.String
message1='Hello World'
print(message1)

message2="Bobby's World"
print(message2)

message3='Bobby\'s World'
print(message3)

message4="""Bobby's World
I want to go back"""
print(message4)

print(len(message4))

print(message1[10])
print(message1[:5])
print(message1[6:])


print(message1.lower())
print(message1.upper())
print(message1.count('l'))
print(message1.find('World')) # start at which index
print(message1.find('Universe')) # cannot find any of them

# Replace first argument with the second argument
newMessage=message1.replace('World','Universe')
print(newMessage)

greeting='Hello'
name='Mike'
message=greeting+', '+name + '. Welcome!' 
message='{},{}. Welcome!!'.format(greeting, name)
message=f'{greeting}, {name.upper()}. Welcome!!!'
print(message)

# see all the method for a variable
#print(dir(name))

# How to use it
#print(help(str))
#print(help(str.startswith))

print(name.startswith('Mi',0,2))

##############################################################################
print('##############################################################################')
##2. float
num=3
print(type(num))

print(3//2) # floor 
print(3 * 2 + 1)

num=1
num=num+1
print(num)

print(abs(-3))
print(round(3.75, 1))

num_1=3
num_2=2

print(num_1==num_2)
print(num_1<num_2)

num_1='100'
num_2='200'

num_1=int(num_1)
num_2=int(num_2)
print(num_1+num_2)

##############################################################################
##3. list, tuple, sets

courses=['History','Math','Physics','CompSci']
print(courses)
print(courses[-2])
print(courses[-2])
print(courses[0:3])
print(courses[2:])
print(courses[:])

# append
courses.append('Art')
print(courses[:])

# insert: add a list to another list. result is a list in another list
courses_2=['Art','Education']
#courses.insert(0,'Chinese')
#courses.insert(0,courses_2)
print(courses[:])


# extend: add a list to another list. result is a longer list!
courses.extend(courses_2)
print(courses)

## remove elements
courses.remove('Math')
popped=courses.pop() # remove the last one
print(popped)
print(courses)

# reverse
courses.reverse()
print(courses)

# sort list and original is changed
courses.sort()
print(courses)

nums=[1,5,2,4,3]
nums.sort(reverse=True)
print(nums)

# sorted function, doesnt change original list
nums=[1,5,2,4,3]
sorted_nums=sorted(nums)
print(nums)
print(sorted_nums)

#print(sorted_courses)
print(max(nums))
print(sum(nums))

# find the index

courses=['History','Math','Physics','CompSci']
print(courses.index('CompSci'))
print('Math' in courses)

for item in courses:
    print(item)
    
for index, course in enumerate(courses, start=1):
    print(index, course)
    
course_str=' - '.join(courses)
print(course_str)

new_list=course_str.split(' - ')
print(new_list)

## tuples
# cannot modify
list_1=['History','Math','Physics','CompSci']
list_2=list_1
print(list_1)
print(list_2)
list_1[0]='Art'
print(list_1)
print(list_2)

tuple_1=('History','Math','Physics','CompSci')
tuple_2=list_1
print(tuple_1)
print(tuple_2)
#tuple_1[0]='Art'  # cannot modify
print(tuple_1)
print(tuple_2)


# Sets
cs_courses={'History','Math','Physics','CompSci','Math'}
print(cs_courses)

# membership test
print('Math' in cs_courses)

art_courses={'History','Math','Art','Design'}
print('Math' in cs_courses)

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

# empty list and set
empty_list=[]
empty_list=list()

# empty tuple
empty_tuple=()
empty_tuple=tuple()

# empty set
empty_set=set()
empty_set={} # this is wrong! This is actually a dictionary

# dict
empty_dict={}


###############################################################################
## 5. dictionary
student={'name':'John','age':'25','courses':['math','CompSci']}
print(student['name'])
print(student['courses'])
student['phone']=['555-555-5555']
student['name']='Jane'
#print(student.get('name','Not Found'))
print(student)

# use update to update the dictionary
#student.update({'name':'Jane','age':26,'phone':'555-555-5555'})

# delete
# del student['age']

age=student.pop('age')
print(student)
print(age)

###############################################################################
print('###############################################################################')
student={'name':'John','age':'25','courses':['math','CompSci']}
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)
    
for key, value in student.items():
    print(key, value)
###############################################################################
print('###############################################################################')

language='Java'      
if language=='Python':
    print('Conditional is Python')
else:
    print('No match')

###############################################################################
print('###############################################################################')

a=[1,2,3]     
b=[1,2,3]
print(id(a))
print(id(b))
print(a is b)

b=a
print(a is b)

# False Values:
# False
# None
# Zero
# Any empty sequence E.g., '', (), []
# Any empty mapping. E.g., {}


condition=10
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


###############################################################################























































