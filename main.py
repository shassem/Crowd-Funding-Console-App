from registeration import *
from login import *

def mainmenu():
    choice=input("Enter r to register or l to login")
    if choice == "r":
        reg()
    elif choice == "l":
        lgin()
    else:
        print("Choose correctly.")
        return mainmenu()

#regproj()
mainmenu()