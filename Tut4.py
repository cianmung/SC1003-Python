
num = int(input("Please enter pattern width: "))
for i in range(1,num):
    for j in range(i):
        print("*",end="")
    print()
for i in range(num,0,-1):
    for j in range(i):
        print("*",end="")
    print()