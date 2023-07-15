# Program to find the factorial of the numbers

n = int(input("Enter a number: "))
fact = 1
if(n<0):
    print("Factorial cannot be found for negative or zero values")
elif(n==0):
    print("Factorial for",0," is ",1)
else:
    for i in range(1,n+1):
        fact=fact*i
print("The Factorial of ",n," is ",fact)


# Program to find the factorial of the numbers using recursion

# def fact(num):
#     if num == 0:
#         return 1
#     return num*fact(num-1)
# num=int(input("Enter a number: "))
# print(fact(num))