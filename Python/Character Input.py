"""
Character Input excercise
Saturday, 23 September 2017
10:58 - 11 : 07 

Create a program that asks the
user to enter their name and their age. Print out
a message addressed to them that tells them the
year that they will turn 100 years old
"""

name = str(input("Give me your name! "))
age = int(input("Hey "+ name +", Give me your age! "))

answer = str((age + 100))
print("In a Hundred Year, your age will be : "  + answer)
