from registeration import *
from datetime import datetime



def savinfo(info):
    try:
        f=open("database.txt","a")
    except:
        print("Error occured")
        return False
    else:
        fr=open("database.txt")
        if info[2] in fr.read():
            fr.close()
            print("This email already exists")
            return False
        z= ":".join(info)
        f.write(f"{z}\n")
        f.close()
        return True

def check(info):
    file = open("database.txt")
    if info in file.read():
        file.close()
        return True
    else:
        file.close()
        return False

def extract(info):
    file = open("database.txt")
    lines = file.readlines()
    for row in lines:
        alll=row.strip('\n').split(':')
        if alll[2] == info:
            return alll
    
    

def savproj(info,user):
    #x = user.split(':')
    f = open(f"{user[0]}-projects.txt", "a")
    z = ":".join(info)
    f.write(f"{z}\n")
    f.close()
    return True

def enterrstrp(message):
    y=input(message)
    if y.isspace() or not y:
        print("Please enter a valid string")
        return enterrstrp(message)
    return y


#view,edit,delete,search

def searchproj(title,user):
    projects=viewproj(user)
    # print(projects)
    # title=enterrstrp("Which title do you want to search for: ")
    for row in projects:
        op=row.strip('\n').split(':')
        if op[0] == str(title):
            # proj_index = projects.index(row)
            # print(f"project found at index {proj_index}")
            return row
    else:
        print("project not found")
        return False

def projindex(title,user):
    projects=viewproj(user)
    # print(projects)
    # title=enterrstrp("Which title do you want to search for: ")
    for row in projects:
        op=row.strip('\n').split(':')
        if op[0] == str(title):
            proj_index = projects.index(row)
            # print(f"project found at index {proj_index}")
            return proj_index
    else:
        print("project not found")
        return False




def viewproj(user):
    try:
        f = open(f"{user[0]}-projects.txt")
    except:
        print("Error!")
        return user
    else:
        z=f.readlines()
        f.close()
        # z=list(z.strip('\n').split(':'))
        print(z)
        return z

def writetoproj(value,user):
    try:
        fileobj = open(f"{user[0]}-projects.txt", "w")
    except Exception as e:
        print(e)
        return False
    else:
        fileobj.writelines(value)
        fileobj.close()
        return True




def editpro(user):
    allprojects=viewproj(user)
    title=enterrstrp("Enter the title you want to edit: ")
    row=searchproj(title,user)
    if row:

        row=list(row.strip('\n').split(":"))
        try:
            i = int(input("1 title, 2 details, 3 total target, 4 start time, 5 end time: "))
        except:
            print("Please enter a suitable number")
            return editpro(user)
        else:
            if i in (1,2):
                print (f"the value you want to change is {row[i-1]}")
                new=enterrstrp("Enter the new value: ")
            elif i == 3:
                print (f"the value you want to change is {row[i-1]}")
                new=entertarget("Enter the new value: ")
            elif i == (4,5):
                print (f"the value you want to change is {row[i-1]}")
                new=settime("Enter the new value: ")
                if i == 5:
                    if row[3] > new:
                        print("Ending date can't be before the starting date")
                        return editpro(user)
            else:
                print("Enter a suitable number")
                return editpro(user)

            ind=projindex(title,user)
            # print(ind)
            row[i-1]=new
            # print(row)
            row=":".join(row)
            # print(row)
            allprojects[ind] = f"{row}\n"
            outp=writetoproj(allprojects,user)
            if outp:
                print("Project edited.")
    else:
        return editpro(user)    

        
def deletepro(user):
    allprojects=viewproj(user)
    title=enterrstrp("Enter the title you want to delete: ")
    row=searchproj(title,user)
    if row:
        # row=list(row.strip('\n').split(":"))
        ind=projindex(title,user)
        del allprojects[ind]
        outp=writetoproj(allprojects,user)
        if outp:
            print("Project deleted")
    else:
        return deletepro(user)



def searchbydate(user):
    projects=viewproj(user)
    inputt=settime("Search by starting date: ")
    for row in projects:
        op=row.strip('\n').split(':')
        if op[3] == inputt:
            return print(row)
    else:
        print("project not found")
        return False

# def editproj(ip,user):
#     ch=searchproj(ip,user):
#     if ch:
#         choice = input("1 title, 2 details, 3 total target, 4 start time, 5 end time: ")
#         if choice == '1':
#             choice = int(choice)
#             try:
#                 f=open(f"{user[0]}-projects.txt")
#             except:
#                 print("Error occured")
#                 return False
#             else:

#                 z= ":".join(ip)
#                 f.write(f"{z}\n")
#                 f.close()
#                 return True




    #try:        
    #    f = open(f"{user[0]}-projects.txt")
    #except:
    #    print("Error!")
    #    return user
    #else:
    #    title=enterrstrp("Enter the title of the project you want to edit: ")
    #    ind=searchproj(title,user)
    #    if ind:
    
            



def settime(message):
    try:
        y=datetime.strptime(input(message), "%d-%m-%Y").date()
    except:
        print("Error!")
        return settime(message)
    else:
        y=y.strftime('%d-%B-%Y')
        return y


def entertarget(message):
    y=input(message)
    if y.isdigit():
        return y
    print ("Please enter a valid number.")
    return entertarget(message)
