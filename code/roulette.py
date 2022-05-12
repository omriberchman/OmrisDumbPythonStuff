import random
plays = int(input("How many tries you want? "))
min = int(input("Enter the min number : "))
max = int(input("Enter the max number : "))
num = 1
while num<plays:
    rannum = random.randint(min, max)
    print("Guess the number! ")
    answer = int(input("you have "+str(plays)+" tries. Insert a number between "+str(min)+"-"+str(max)+" "))

    if rannum == answer:
        print("You won!")
        num += 20
    else:
        print("Too bad! try again!")
        num += 1
        plays -= 1
