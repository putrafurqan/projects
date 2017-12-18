"""
First Input Project
22 Sept 09.01 a.m

"""
import os
#Login
user = ['furqanriansyah']
passwd = ['12052004']
Username = str(input("Username : "))
Password = str(input("Password : "))
arg1 = "Wrong Username or Password"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def login(usn,pwd,user,passwd,arg1):
    if (Username in user and Password in passwd):
        print("Acces Granted")
        clear_screen()
        main()
    else:
        print(arg1)
        login_try = 3
        for users in Username and Password :
            usn
            pwd
            if Username in user and Password in passwd:
                print(arg1)
                break
            else:
                print()
                login_try -= 1
                if login_try == 0 :
                    print(arg1)
                    exit()

def main():
    os.system("python3 activity.pyc")
login(Username,Password,user,passwd,arg1)




#
