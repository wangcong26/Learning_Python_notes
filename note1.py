# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:51:46 2019
This is some notes from the book "Learning Python"

@author: swang
"""

# import math and random
import math
print(math.pi)

import random
random.random()
random.choice([1,3,4,6,'string'])

###############################################################################
# Sequence Operations
S='Spam'
# Print last one letter
print(S[-1])
# Negative indexing, the hard way
print(S[len(S)-1])
# The second-to-last item from the end
print(S[-2])

print(S[0:3])
print(S[:3])

# everything but last one
print(S[0:-1])
print(S[0:3])
print(S[:3])

# concatenate
print(S+'xyz')

# Change to a list
L=list(S)
L[1] = 'c'

# Join without any delimiter for the list, only for string
''.join(L)

# A bytes/list hybrid (ahead)
B = bytearray(b'spam')

# replace and find
S = 'Spam'
print(S.replace('pa', 'XYZ'))
print(S)

###############################################################################
line = 'aaa,bbb,ccccc,dd'
line.split(',')


S = 'spam'
# Uppercase for all the letters
print(S.upper())
# Capitalize first letter
print(S.capitalize())
# remove whitespace
print(line.rstrip())
print(line.rstrip().split(','))

# Formatting Digits, padding, signs
print('{:,.3f}'.format(296999.2547))

###############################################################################
# Pattern Matching

import re
match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
match.group(1)

re.split('[/:]', '/usr/home/lumberjack')

###############################################################################
# List

# A list of three different-type objects
L = [123, 'spam', 1.23]

# Number of items in the list
print(len(L))

# Indexing by position
L[0] 
L[:-1]
L + [4, 5, 6]

# Growing: add object at end of list
L.append('NI')

# Shrinking: delete an item in the middle
L.pop(2)

# Change the M itself
M = ['bb', 'aa', 'cc']
M.sort() # sort
M.reverse() # reverse

M = [[1, 2, 3], # A 3 × 3 matrix, as nested lists
[4, 5, 6], # Code can span lines if bracketed
[7, 8, 9]]

# Comprehensions List
col2=[row[1] for row in M] # this means give me row[1] for every row in M. It read row by row in M.
print(col2)

# Collect a diagonal from matrix
diag = [M[i][i] for i in [0, 1, 2]]

# Repeat characters in a string
doubles = [c * 2 for c in 'spam'] 
print(doubles)

# Create list using range
list(range(4))
list(range(-6, 7, 2))
newList1=[[x ** 2, x ** 3] for x in range(4)]
newList2=[[x,x/2,x*2] for x in range(-6,7,2) if x>0]

# Compute sum generator using Comprehensive list with parenthesis
G=(sum(row) for row in M)

# Use map to compute the sum of each row in M as a list
list(map(sum,M))

# Use map to compute the sum of each row in M as a set
{sum(row) for row in M}

# Creates key/value table of row sums
pair={i : sum(M[i]) for i in range(3)}
print(pair)

# Mapping Operations############################################################
# Map
D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D)
# use key
D['food']
D['quantity'] += 1 # Add 1 to 'quantity' value
print(D)

# create a new dictionary
bob1 = dict(name='Bob', job='dev', age=40) #keywords
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40])) # Zipping

# Nesting
rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40.5}


rec['name']['last'] # output 'Smith'

# Assign new key
D['e'] = 99 

# get all the keys
D = {'a': 1, 'z': 5, 'c': 3}
keys=list(D.keys())
print(keys)

# sort keys and original keys gets changed.
keys.sort()
print(keys)

# use sorted() to sort directly and original dictionary changed.
aa = {'a': 1, 'z': 5, 'c': 3}
print(aa)
sorted(aa)
print(aa)

# Tuples ######################################################################
T=(1,2,3,4)
T+(5,6)

T.index(4) # Tuple methods: 4 appears at offset 3
T.count(4) # 4 appears once

T=(2,)+T[1:] # Make a new tuple for a new value

# Files #######################################################################


# Other types #################################################################
X = set('spam') # Make a set out of a sequence. This is a set!!
Y = {'h', 'a', 'm'} # Make a set with set literals. This is a set!!
X, Y # A tuple of two sets without parentheses
X & Y # Intersection
X | Y # Union
X - Y # Difference things in X but not in Y
Y - X # things in Y but not in X


list(set([1, 2, 1, 3, 1])) # Filtering out duplicates (possibly reordered)

set('spam') - set('ham') # Finding differences in collections

set('spam') == set('asmp') # Order-neutral equality tests (== is False)

result='p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham']

# import decimal
import decimal 
d = decimal.Decimal('3.141') # Decimals: fixed precision
d+2


























