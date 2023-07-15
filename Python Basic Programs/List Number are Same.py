# Program to Check if the first and last number of a list is the same

list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	elem = int(input())
	list.append(elem)
print(list)
first=list[0]
last=list[-1]
if first == last:
    print("The First and last Number in lists are equal")
else:
    print("The First and last Number in lists are not Equal")