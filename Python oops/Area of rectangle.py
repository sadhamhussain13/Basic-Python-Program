# create a class
class Rectangle:
    length = float(input("Enter length "))
    breadth = float(input("Enter breadth "))
    
    # method to calculate area
    def calculate_area(self):
        print("Area of Rectangle =", self.length * self.breadth)

# create object of Rectangle class
rect = Rectangle()

# access method inside class
rect.calculate_area()