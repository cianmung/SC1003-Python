from itertools import count


count = 0
while True:
    str = input("enter a string: ")
    lastLetter = str[-1]
    for letter in str:
        if letter == 'a':
            count +=1
        elif letter == lastLetter:
            break
    print(count , "strings with letter 'a'")

