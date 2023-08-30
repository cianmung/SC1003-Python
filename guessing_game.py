import random

print("Please select one of the following quizzes:\n\t1.Number guessing\n\t2.Calculate sum")
selectedGame = int(input())
if selectedGame == 1:
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
                print('Wrong input format. Please try again.')
                if count < 3:
                    guess = input("Enter an integer from 1 to 9: ")
                    if guess.isnumeric():
                        guessCount+=1
    else:
        print("Sorry, you exceed the trial limit. Failed.")
elif selectedGame == 2:
    randomNumber = random.randint(55, 66)
    print('Please calculate the sum of 5 integers start from {}'.format(randomNumber))
    totalNumber = 0
    count = 0
    while(count < 5):
        totalNumber += randomNumber + count
        count += 1
    answer = int(input("Please enter your answer: "))
    print(totalNumber)
    if(answer == totalNumber):
        print("You can start the game now")
    else:
        print("Sorry, wrong answer. Failed.")
else:
    print('Wrong option. Bye')




