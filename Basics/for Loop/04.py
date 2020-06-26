"""
Copyright 2020. 
This is a python problem solution.
Author : Vishnuvardhan Reddy
Python Basics - For Loops : Problem 4
"""
num = int(input("Enter a non negative number:"))
or_num = num
rev_num=0
count = 0
while num!=0:
    rem = num%10
    rev_num = rev_num*10 + rem
    num=int(num/10)
    if num>=0:
        count = count+1
print("Reverse Num = ",format(rev_num))
if(rev_num == or_num):
    print("palindrome")
else:
    print("not palindrome")
print("No of digits :",format(count))
