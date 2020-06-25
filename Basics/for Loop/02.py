"""
Copyright 2020. 
This is a python problem solution.
Author : Vishnuvardhan Reddy
Python Basics - For Loops : Problem 1
"""
from numpy import arange

start =  int(input("Enter start value :"))
stop = int(input("Enter stop value:"))
step = float(input("Enter the step size:"))
if abs(start - stop) < step:
    print("Increase the range or decrease the step size...")
    exit()
else :
    for i in arange(start, stop, step):
        print(i, end="\n")
