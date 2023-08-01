# ====================================================================================
# Author: Trung Le 
# Created Date: 06/27/2023
# Simple Python app to get username and domain from an email
# 07/28/2023: Trung - Add email validation
#=====================================================================================
import re 

# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# Method: emailChecking
# Input: string email
# output: True/False
def emailChecking(email):
    if(re.fullmatch(regex, email)):
        print("Valid Email")
        return True
    else:
        print("Invalid Email")
        return False

# Method: emailslicer
# Input: string email
# output: string username and string domain
def emailslicer(email):
    # get list of username and domain
    listwords = email.split('@')
    username = listwords[0]
    domain = listwords[1]
    print("Your username is %s\nand your domain is %s" % (username, domain))   

# main
# Driver Code
if __name__ == "__main__":
    option = True
    while option == True:
        # display instruction of app
        print("========================================================================")
        print("1. Email slicer - Email, username, and domain will be auto saved to file.")
        print("2. Exit")
        print("========================================================================")
        # get choice and convert from string input to int
        choice = int(input("Your choice (1 or 2): ").strip())
        if choice == 1:
            # get email from user input
            email = input("Enter your email: ").strip()
            # repeat asking until get a valid email
            while(emailChecking(email) == False):
                email = input("Enter your email: ").strip()
                # get result for slicing email
                emailslicer(email)
        else:
            option = False
            break
