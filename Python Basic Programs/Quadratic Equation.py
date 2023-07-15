# Program to Solve the quadratic equation ax**2 + bx + c = 0
# import complex math module

import cmath
a = float(input("Enter a number: "))
b = float(input("Enter b number: "))
c = float(input("Enter c number: "))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))     #string formatting