# Program to Display numbers divisible by 5 from a list

list=[]
n=int(input("Enter the number of elements in your List: "))
for i in range(0,n):
    num = int(input()) 
    list.append(num)
    if(num%5==0):
        print(num," is divisible by 5")
    else:
        print(num," is not divisible by 5")
print(list)



# Program to find number divided by 5 using function

# def div(num):
#     if num%5==0:
#         return ('number divisible by 5')
#     else:
#         return ("number not divisible by 5")
# n=int(input())
# print(div(n))