from Lab2 import guessingGame
from Lab3 import existingUsers, userRegistration, userLogin

selectOption = int(input("Please select one of the following options:\n\t1.User registration\n\t2.User Login\t\n3.Play the game as a guest\n"))

if selectOption == 1:
    userRegistration()
elif selectOption == 2:
    userLogin()
elif selectOption == 3:
    guessingGame()
else:
    print("Wrong Option")