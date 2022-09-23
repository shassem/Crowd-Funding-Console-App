from database import savinfo, savproj
from getpass import getpass
from datetime import datetime

def enterstr(message):
    y = input(message)
    if y.isspace() or not y or y.isdigit():
        print("Please enter a string with no digits.")
        return enterstr(message)
    return y

def enterstrp(message):
    y=input(message)
    if y.isspace() or not y:
        print("Please enter a valid string")
        return enterstrp(message)
    return y

def enternum(message):
    y = input(message)
    if y.isdigit() and y.startswith(('012', '011', '015', '010')) and len(y) == 11:
        #y = int(y)
        return y

    print("Please enter a suitable number.")
    return enternum(message)

def entertarget(message):
    y=input(message)
    if y.isdigit():
        return y
    print ("Please enter a valid number.")
    return entertarget(message)


def entermail(message):
    y = input(message)
    if y.endswith('.com') and '@' in y:
        return y
    print("Please enter a valid email.")
    return entermail(message)

def confpassw(message, password):
    y = getpass(message)
    if y == password:
        print("Password confirmed.")
        return y
    else:
        password=getpass("Error in confirmation, please enter a password again: ")
        return confpassw(message, password)


    
def details():
    fn=enterstr("Enter your first name: ")
    ln=enterstr("Enter your last name: ")
    email=entermail("Enter your email: ")
    password=getpass("Enter your password: ")
    conf=confpassw("Confirm your password: ", password)
    mobilephone=enternum("Enter your egyptian mobile phone: ")
    return fn,ln,email,conf,mobilephone

def reg():
    y = list(details())
    #z= ":".join(y)
    regist= savinfo(y)
    if regist:
        print("Your account is successfully created.")
    else:
        print("ERROR!")
        return reg()

def settime(message):
    try:
        y=datetime.strptime(input(message), "%d-%m-%Y").date()
    except:
        print("Error!")
        return settime(message)
    else:
        y=y.strftime('%d-%B-%Y')
        return y

def setend():
    y=settime("End of project (DD-MM-YYYY): ")
    if y < startt:
        print("The ending time can't be before the starting time.")
        return setend()
    return y



def proj():
    title=enterstrp("Enter the project title: ")
    details=enterstrp("Enter the project details: ")
    totarget=entertarget("Enter the total target (EGP): ")
    global startt
    startt=settime("Start of project (DD-MM-YYYY): ")
    end=setend()
    return title, details, totarget, str(startt), str(end)

def regproj(user):
    y = list(proj())
    regist=savproj(y,user)
    if regist:
        print("Project details are saved.")
    else:
        print("ERROR!")
        return regproj()




