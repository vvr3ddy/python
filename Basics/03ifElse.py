"""
Copyright © VVR 2020
Learn Python by programming on the go
File name          : ifElse.py
Author             : Vishnuvardhan Reddy

"""

def factorial(num) :

    if int(num) == 0 :
        return 1
    elif int(num) > 0 :
        return num*factorial(num-1)
    else :
        return "Enter a non zero number."

n=input("Enter a number greater than zero:")

print(factorial(int(n)))
