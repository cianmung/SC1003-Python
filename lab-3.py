isUpper = False
isLower = False
isDigit = False
isUserExisted = False
existingUsers = {"Test":"Test12345", "Jack":"Test12345","Tom":"Password1"}

print("User registration:")
while isUserExisted == False:
    username = input("Input your user name: ")
    for user in existingUsers:
        if user == username:
            isUserExisted = True
    print(isUserExisted)

while isUpper == False or isLower == False or isDigit == False:
    print("Input your password:")
    print("1.the password has at least one upper case letter")
    print("2.the password has at least one lower case letter")
    print("3.the password has at least one digit")
    password = input()

    for i in password:
        if i.isupper():
            isUpper = True

    for i in password:
        if i.islower():
            isLower = True

    for i in password:
        if i.isnumeric():
            isDigit = True
    if isUpper == False or isLower == False or isDigit == False: 
        print("Your password is weak. Please enter a new password")
else:
    print("Your password is strong enough. User registered.")
    print("The users in the system")
    print(existingUsers)
    