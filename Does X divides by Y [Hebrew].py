print("בדוק אם מספר מתחלק במספר אחר ללא שארית")
num1 = int(input("Enter the first number you want to check: " ))
pre = int(input("Enter second number  you want to check: "))
print("")
num2 = str(num1)
pre1 = str(pre)
print("המספרים שמתחלקים ב"+ pre1 + " ללא שארית ")
for num in range(num1):
    if num%3 == 0:
        print(num)
    else :
        continue
