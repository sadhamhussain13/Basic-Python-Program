# Program to find the square of the numbers in the list

def square(num):
    sq=[]
    for i in range(1,num+1):
        sq.append(i*i)
    return sq
value=int(input("Enter a number: "))
print(square(value))