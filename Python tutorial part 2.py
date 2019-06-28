# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 15:30:49 2019

@author: swang
"""
# simple loops
nums=[1,2,3,4]

for num in nums:
    if num==3:
        print('Found')
        continue
    print(num)
    
for num in nums:
    for letter in 'abc':
        print(num,letter)
        
for i in range(10):
    print(i)
    
x = 0

while x < 10:
    if x==5:
        break
    print(x)
    x += 1


