for each in range(1,21):
    if each % 15 == 0:
        print("FizzBuzz")
    elif each % 3 == 0:
        print("Fizz")
    elif each % 5 == 0:
        print("Buzz")
    else:
        print(each)