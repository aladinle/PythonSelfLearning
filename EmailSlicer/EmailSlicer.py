# ====================================================================================
# Author: Trung Le 
# Date: 06/27/2023
# Console App that gets an email from user input and seperate into username and domain
# 07/28/2023: Trung - Add email validation
#=====================================================================================
import re

# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# Email checking
def emailChecking(email):
    if(re.fullmatch(regex, email)):
        print("Valid Email")
        return True
    else:
        print("Invalid Email")
        return False

def emailslicer(email):
    # get list of username and domain
    listwords = email.split('@')
    username = listwords[0]
    domain = listwords[1]
    print("Your username is %s\nand your domain is %s" % (username, domain))   

# Driver Code
if __name__ == "__main__":
    # get email from user input
    email = input("Enter your email: ").strip()
    # repeat asking until get a valid email
    while(emailChecking(email) == False):
        email = input("Enter your email: ").strip()
    # get result for slicing email
    emailslicer(email)
    
        





