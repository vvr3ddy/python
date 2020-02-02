"""
Copyright © VVR 2020
Learn Python by programming on the go
File name          : forLoop.py
Author             : Vishnuvardhan Reddy

"""

name=input("Enter a String : ")
for i in range(len(name)):
        if name[i]==name[len(name)-i-1]:
            flag = 1
        else :
            flag = 0
if flag == 0:
    print("String is not a palindrome")
else :
    print("String is a palindrome")
