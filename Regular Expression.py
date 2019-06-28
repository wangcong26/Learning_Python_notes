# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 14:19:14 2019

@author: swang
"""

import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
mat
pat
bat
'''

emails='''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

sentence = 'Start a sentence and then bring it to an end'

#1 raw string
print(r'\tTab')

#2 compile method
pattern = re.compile(r'abc', re.I)
pattern = re.compile(r'\.', re.I) # have to escape \.
pattern = re.compile(r'.', re.I) # match any character except new line
pattern = re.compile(r'\d', re.I) # match all the digit
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d', re.I) # match phone number
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d', re.I) # use a character set [-.]
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d', re.I) # start with 800, 900
pattern = re.compile(r'[1-5]', re.I) # set of digits
pattern = re.compile(r'[a-zA-Z]', re.I) # set of letters
pattern = re.compile(r'[^a-zA-Z]', re.I) # not in this set of letters
pattern = re.compile(r'[^b]at', re.I) # not start with b
pattern = re.compile(r'\d{3}.\d{3}.\d{4}') # use quantifier {3} exact number
pattern = re.compile(r'Mr\.?\s[A-Z]\w*') # match anything starting with Mr. or Mr ? - 0 or 1
pattern = re.compile(r'M(r|s|rs).?\s[A-Z]\w*') # use group
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') # use group
matches = pattern.finditer(text_to_search)
for each in matches:
    print(each)

# open a file
#with open('data.txt','r') as f:
#    contents=f.read()
#    matches = pattern.finditer(contents)
#    for match in matches:
#        print(match)



emails='''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com') # use group





















