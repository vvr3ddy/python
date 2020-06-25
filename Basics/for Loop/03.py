"""
Copyright 2020. 
This is a python problem solution.
Author : Vishnuvardhan Reddy
Python Basics - For Loops : Problem 3
"""
import string
for i, c in enumerate(string.ascii_letters):
        if(i % 13 == 0):
            print('\n')
        print(c, end = ", ")
print()
