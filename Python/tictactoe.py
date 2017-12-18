"""
Tic Tac Toe Project
19 October 2017
16:06
"""
def open():
    print"Welcome to Tic Tac Toe Game"

def main():
    while True:
        player = input("Choose :[X/O]").lower
        computer = ""
        if player == "x":
            computer = "o"
            break
        elif player == "o":
            computer = "x"
            break
        else:
            print("[X/O]")

    board = "  A B C \n  _ _ _ \n1|{}|{}|{}|\n2|{}|{}|{}|\n3|{}|{}|{}|".format(a1,b1,c1,a2,b2,c2,a3,b3,c3)
    a1 =
