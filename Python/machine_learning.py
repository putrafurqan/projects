"""
Guess Number project
1 September 2017
10 : 04
"""
import random
false_list = []

def main():
    ans_limit = int(input("Computing Limit: "))
    try_= 0
    answer = int(input("Answer : "))
    while ans_limit > 0:
        start = 610000
        end = 70000000
        ans = int(random.randint(start,end))
        if ans == answer :
            print(false_list)
            print("Compute Succes")
            print("try " + str(try_) + ", answer = " + str(ans))
            break
        elif ans < answer :
            try_ += 1
            ans_limit -= 1
            false_list.append(str(ans) + " S")
            start = start * 0 + ans
        elif ans > answer :
            try_ += 1
            ans_limit -= 1
            false_list.append(str(ans) + " E")
            end = end * 0 + ans
        if ans_limit <= 0 :
            print(false_list)
            print('Failed to compute!')


main()
