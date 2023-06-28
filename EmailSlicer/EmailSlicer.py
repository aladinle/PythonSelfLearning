# get email from user input
email = input("Enter your email: ").strip()
# get list of username and domain
listwords = email.split('@')
username = listwords[0]
domain = listwords[1]
print("Your username is %s\nand your domain is %s" % (username, domain))

