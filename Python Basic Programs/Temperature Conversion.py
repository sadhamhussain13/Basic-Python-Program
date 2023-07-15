# # Python Program to convert temperature in celsius to fahrenheit

# celsius = float(input())
# # calculate fahrenheit
# fahrenheit = (celsius * 1.8) + 32
# print('{0} degree Celsius is equal to {1} degree Fahrenheit' .format(celsius,fahrenheit))

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = int(input("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nEnter your choice: "))

if choice == 1:
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print("Temperature in Fahrenheit:", fahrenheit)
elif choice == 2:
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print("Temperature in Celsius:", celsius)
else:
    print("Invalid choice.")