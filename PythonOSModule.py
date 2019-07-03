# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 08:32:17 2019

@author: swang
"""

import os
from datetime import datetime

#print(dir(os))
#print(os.getcwd())

#change directory
#os.chdir('Downloads')

# print out what's in the directory
#print(os.listdir())

#make a new folder
#os.makedirs('/test')
#print(os.getcwd())
#os.removedirs('Clustering')
#os.makedirs('Clustering') # create a folder under current directory

###############################################################################
#os.rename('data.txt','data2.txt')

#print(os.stat('data.txt'))

###############################################################################
#mod_time=os.stat('data.txt').st_mtime
#print(datetime.fromtimestamp(mod_time))



###############################################################################
# walk through all the directory
#for dirpath, dirnames, filenames in os.walk('C:/Users/swang/Desktop'):
#    print('Current Path: ',dirpath)
#    print('Directory: ',dirnames)
#    print('Files: ',filenames)
#    print()

###############################################################################
#print(os.environ.get('C:/Users/swang/Desktop'))
file_path=os.path.join(os.getcwd(),'test.txt') # join two path together
#print(file_path)

###############################################################################
print(os.path.basename('/tmp/test.txt'))
os.path.dirname('/tmp/test.txt')
os.path.split('/tmp/test.txt')
os.path.exists('/tmp/test.txt') # check if this path exists
os.path.isfile('/tmp/test.txt')
os.path.splitext('/tmp/test.txt') # split file name


























