import random
import re

existingUsers = {"Test":"Test12345", "Jack":"Test12345","Tom":"Password1"}

def getUserChoice():
    choice = int(input('''Please select one of the following options:
    1. User registration
    2. User Login
    3. Play the game as a guest\n'''))
    return choice

def guestQuiz():
    quizChoice = chooseQuiz()
    isPass = takeQuiz(quizChoice)
    if isPass:
        print("Congratulations. You can start the game.")

def chooseQuiz():
    choice = int(input('''Dear Guest, you have to pass one quiz to play the game.
    Please select one of the following quizzes:
    1. Number guessing
    2. Calculate sum\n'''))
    return choice

def guessingNumber():
    randomNumber = random.randint(1, 9)
    count = 0
    guessCount = 0
    guess = input("Enter an integer from 1 to 9: ")
    if guess.isnumeric():
        guessCount+=1
    while count < 3:
            count+=1
            if guess.isnumeric():
                guess = int(guess)
                if guess < randomNumber:
                    print ("guess is low")
                    if count < 3:
                        guess = input("Enter an integer from 1 to 9: ")
                        if guess.isnumeric():
                            guessCount+=1
                elif guess > randomNumber:
                    print ("guess is high")
                    if count < 3:
                        guess = input("Enter an integer from 1 to 9: ")
                        if guess.isnumeric():
                            guessCount+=1
                else:
                    if guessCount <= 1:
                        print ("Congratulations. You guessed it by {} trial!".format(guessCount))
                    else:
                        print ("Congratulations. You guessed it by {} trials!".format(guessCount))
                    print()
                    print("You can start the game now")
                    break
            else: 
                if count < 3:
                    print('Wrong input format. Please try again.')
                    guess = input("Enter an integer from 1 to 9: ")
                    if guess.isnumeric():
                        guessCount+=1
                elif count >= 3:
                    print('Wrong input format.')
    else:
        print("Sorry, you exceed the trial limit. Failed.")

def calculateSum():
    randomNumber = random.randint(55, 66)
    print('Please calculate the sum of 5 integers start from {}'.format(randomNumber))
    totalNumber = 0
    count = 0
    while(count < 5):
        totalNumber += randomNumber + count
        count += 1
    answer = int(input("Please enter your answer: "))
    if(answer == totalNumber):
        print("You can start the game now")
    else:
        print("Sorry, wrong answer. Failed.")

def takeQuiz(choice):
    if choice == 1:
        isPass = guessingNumber()
    elif choice == 2:
        isPass = calculateSum()
    return isPass

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
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
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

def main():
    choice = getUserChoice()
    if choice == 1:
        userRegistration()
    elif choice == 2:
        userLogin()
    elif choice == 3:
        guestQuiz()

main()