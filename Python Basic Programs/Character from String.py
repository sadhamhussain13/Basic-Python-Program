#Program to Print characters from a string that are present at an even index number

word=str(input("Enter a word: "))
print("The original words are: ",word)
x=word
for i in word[0::2]:
    print (i)