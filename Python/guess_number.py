"""
Guess Number project
1 September 2017
10 : 04
"""
import random

def main():
    print("Guess a number between 1 - 100")
    ans_limit = 5
    answer = random.randint(1, 100)
    while ans_limit > 0:
        try:
            ans = int(input("Answer : "))
        except ValueError:
            print("That's not a number!")
            break
        if ans == answer :
            print("Correct")
            break
        elif ans < answer :
            ans_limit -= 1
            print("Bigger,{} Try Again".format(ans_limit))
        elif ans > answer :
            ans_limit -= 1
            print("Smaller,{} Try Again".format(ans_limit))
        if ans_limit <= 0 :
            print('You Lose!')
            print('Correct Number is {}'.format(answer))
            try_again = str(input("Try Again? (Y/N)").upper())
            if try_again == "Y":
                main()
            elif try_again == "N":
                print("Bye!")
                break

main()
