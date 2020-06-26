"""
Copyright 2020. 
This is a python problem solution.
Author : Vishnuvardhan Reddy
Python Basics - For Loops : Problem 5
"""
num = int(input("Enter a non negative number:"))
res = [int(i) for i in str(num)] #convert to a list
print(res)
check = int(input("Enter the number u want to check the occurence frequency:"))
print("Frequency of {} is {}".format(check, res.count(check)))
