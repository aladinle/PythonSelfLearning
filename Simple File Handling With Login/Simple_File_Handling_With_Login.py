#==========================================================================================#
# File: Simple File Handler with Login. Need to do:                                        #
# 1) Try to create a new file if not exist.                                                #
# 2) Enter username and password to log in                                                 #
# 3) Return message if not correct. If correct login info in file, then go welcome username#
#==========================================================================================#
import os.path

path_file = "D:/login_file.txt"

def checkFileExist():
     # open file if exist.
    check_file = os.path.isfile(path_file)
    if(check_file):
        print("File is exist")
        return True
    else: 
        print("File is not exist")
        return False

def addNewAccount(username, password):
    account_file = open(path_file, "+a")
    account_file.write("\n" + username + ":" + password)
    account_file.close()

def login(username, password):
    # case file is exist
    if(checkFileExist()):
        # read login_file.txt and get all accounts as lines
        accounts = open(path_file, "r")
        # flag to check user exist
        isUserExist = False
        for line in accounts:
            usr, pwd = line.replace("\n", "").split(":")
            if(username == usr) and (password == pwd):
                print("User is exist")
                isUserExist = True
                break
            else:
                continue
        # case user is not exist, ask if want to add new user to file
        if (isUserExist == False):
            print("User is not exist")
            choice = input("Do you want to add new account? (Y or N)")
            if(choice.lower() == "y"):
                addNewAccount(username,password)
    else:
        # case file is not exist
        # create a new file
        print("creating a new file login_file.txt...")
        account_file = open(path_file, "x")


if __name__ == "__main__":
    isStop = False
    while(isStop == False):
        username = input("Enter username: ")
        password = input("Enter password: ")
        login(username, password)
        confirm = input("Do you want to continue??? (Y or N): ")
        if(confirm.lower() == "n"):
            isStop = True
        else:
            continue





