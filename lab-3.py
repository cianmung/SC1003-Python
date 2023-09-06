import re
existingUsers = {"Test":"Test12345", "Jack":"Test12345","Tom":"Password1"}

def userRegistration():
    isUpper = False
    isLower = False
    isDigit = False
    isSpecial= False
    isUserExisted = True
    print("User registration:")
    while isUserExisted:
        username = input("Input your user name: ")
        if(username in existingUsers):
            print("The user exists. Please choose another user name.")
        else:
            isUserExisted = False

    while isUpper == False or isLower == False or isDigit == False or isSpecial == False:
        print("Input your password:")
        print("1.the password has at least one upper case letter")
        print("2.the password has at least one lower case letter")
        print("3.the password has at least one digit")
        print("4.the password has at least one special character")
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]');
        password = input()

        isUpper = any(i.isupper() for i in password)
        isLower = any(i.islower() for i in password)
        isDigit = any(i.isnumeric() for i in password)
        isSpecial = regex.search(password) != None

        if isUpper == False or isLower == False or isDigit == False or isSpecial == False: 
            print("Your password is weak. Please enter a new password")
    else:
        print("Your password is strong enough. User registered.")
        print("The users in the system")
        existingUsers[username] = password
        print(existingUsers)

def userLogin():
    username = input("Input user name: ")
    if username in existingUsers:
        password = input("Input password: ")
        while(existingUsers[username] != password):
            password = input("Wrong password, input again: ")
        else:
            print("Welcome back, {}, You can start the game.".format(username))

    else: 
        print("User not existing.")

print("Please select one of the following options:\n\t1.User registration\n\t2.User Login")
selectMode = int(input())

if selectMode == 1:
    userRegistration()
elif selectMode == 2:
    userLogin()
else:
    print('Wrong choice')