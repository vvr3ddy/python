"""
Copyright 2020. 
This is a python problem solution.
Author : Vishnuvardhan Reddy
Python Basics - For Loops : Problem 5
"""
x = int(input("Enter x:"))
y = int(input("Enter y:"))
n1,n2 = x,y
while (y):
    x, y = y, x % y

print("HCF = {}".format(x))
print("LCM = {}".format(n1*n2/x)) #Use N1*N2 = LCM*GCD
