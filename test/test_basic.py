# --------------------------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-

# Simple algorithms to test python language

# Algorithm: Functionality list
# 	Pfunction [2019-05-13]: Pfunction was an early attempt to run a .py
# 	   file by itself.  Originally i just wrote a function and tried to
#      run it, but nothing happened.  I then researched the issue and
#      learned that i needed to call the function to get it to run.
# 	   language ref: https://www.w3schools.com/python/python_functions.asp
# --------------------------------------------------------------------


# So this code works, it'll run a function and it's callout.  Now add some
#   Functionality.
def Pfunction():
    print('Pfunction')
    return 'Test function'

print(Pfunction())

# So let's add a letter to a string.
def Pfunction1(letter):
#    letter += letter + "a"      # so both of these "return" 'a'
    letter += "a"                # the second is cleaner.
    return letter                # remember to use RETURN.

print(Pfunction1(letter=""))    #should print 'a'




