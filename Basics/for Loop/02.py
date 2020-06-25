"""
Copyright 2020. 
This is a python problem solution.
Author : Vishnuvardhan Reddy
Python Basics - For Loops : Problem 2
"""

start =  int(input("Enter start value :"))
stop = int(input("Enter stop value:"))
step = int(input("Enter the step size"))
if abs(start - stop) < step:
    print("Increase the range or decrease the step size...")
    exit()
else :
    for i in range(start, stop, step):
        print(i, end="\n")
