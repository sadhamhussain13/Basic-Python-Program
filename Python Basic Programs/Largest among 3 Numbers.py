# Progarm for finding largest among three numbers

a=int(input("Enter a number 1: "))
b=int(input("Enter a number 2: "))
c=int(input("Enter a number 3: "))
if (a>b) and (a>c):
    print("You are entered first number " + str(a) + " is the largest number.")
elif(b>c) and (b>a):
    print("You are entered second number " + str(b) + " is the largest number.")
else:
    print("You are entered third number " + str(c) + " is the largest number.")
