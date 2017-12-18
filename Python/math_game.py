"""
Math Game
16 oct 2017
"""
import random
from math_dict import ops
import sys
import os

def start():
    mode = input("Welcome to MATH GAME\nChoose difficulty :\nEasy\nMedium\nHard\Expert\n> ").lower()
    if mode == "easy":
        easy(score)
        ()
    if mode == "medium":
        medium(score)
        ()
    if mode == "hard":
        hard(score)
        ()

score = 0

def easy(score):
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    oper = random.choice(["+","-","/","*"])
    quest = int(ops[oper](num1,num2))
    if num1 % num2 != 0:
        easy(score)
    elif oper == "/" or "*" and num1 and num2 > 10:
        easy(score)
    else:
        try:
            answer = int(input("{} {} {} = ".format(str(num1),oper,str(num2))))
        except ValueError:
            print("That's not a number")
            sys.exit()
        if answer == quest:
            score += 1
            print("Correct")
            easy(score)
        else:
            print("False\nCorrect answer = {}\nTotal Score = {}".format(quest,score))

def medium(score):
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    oper = random.choice(["+","-","*","/"])
    quest = int(ops[oper](num1,num2))
    if num1 % num2 != 0:
        medium(score)
    elif (oper == "*") and (num1 or num2 > 30):
        medium(score)
    else:
        try:
            answer = int(input("{} {} {} = ".format(num1,oper,num2)))
        except ValueError:
            print("That's not a number")
            sys.exit()
        if answer == quest:
            score += 1
            print("Correct")
            medium(score)
        else:
            print("False\nCorrect answer = {}\nTotal Score = {}".format(quest,score))

def hard(score):
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    oper = random.choice(["+","-","*","/"])
    quest = int(ops[oper](num1,num2))
    if num1 % num2 != 0 and oper == "/":
        hard(score)
    else:
        try:
            answer = int(input("{} {} {} = ".format(num1,oper,num2)))
        except ValueError:
            print("That's not a number")
        if answer == quest:
            score += 1
            print("Correct")
            hard(score)
        else:
            print("false\nCorrect Answer = {}\nTotal Score = {}".format(quest,score))

def expert(score):
    num1 = random.randint(1,500)
    num2 = random.randint(1,500)
    oper = random.choice(["+","-","*","/"])
    quest = int(ops[oper](num1,num2))



start()
