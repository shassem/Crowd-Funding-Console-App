from database import *
from getpass import getpass
from registeration import *

def lgin():
    mail=entermail("Enter your email: ")
    passs=getpass("Enter your password: ")
    if check(f'{mail}:{passs}'):
        global extracted
        extracted=extract(mail)
        print("You are logged in.")
        return user()


    else:
        print("You have entered an incorrect mail or password. Please try again!")
        return lgin()

def user():
    choice=input("Enter r to register project, v to view projects, e to edit, d to delete, s to search using date: ")
    if choice == 'r':
        return regproj(extracted)
    elif choice == 'v':
        return viewproj(extracted)
    elif choice == 'e':
        return editpro(extracted)
    elif choice == 'd':
        return deletepro(extracted)
    elif choice == 's':
        return searchbydate(extracted)
    else:
        print("Enter a valid character")
        return user()