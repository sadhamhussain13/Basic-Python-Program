# Program for finding prime numbers

a=int(input("Enter a number: "))
if (a>1):
    for i in range(2,a):
        if(a % i ==0):
            print(str(a) + " is not a prime number.")
            print(i," times" ,a//i ," is " ,a)
            break
    else:
        print(str(a) + " is a prime number.")
if (a==1):
    print(str(a) + " is a prime number.")