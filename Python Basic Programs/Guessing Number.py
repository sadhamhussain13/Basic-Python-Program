# program to find the random number

import random
num=random.randint(1,5)

guess=int(input('Guess the number less than 5: '))
while num!=guess:
    if guess > num:
        print("your guess is greater")
    else:
        print("your guess is lower")
    guess=int(input('Guess again: '))
print('you won')