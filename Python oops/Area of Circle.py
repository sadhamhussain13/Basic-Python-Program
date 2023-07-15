class Triangle:
    length = float(input("Enter length "))
    breadth = float(input("Enter breadth "))
    
    # method to calculate area
    def calculate_area(self):
        print("Area of triangle =", 0.5 * self.length * self.breadth)

# create object of Triangle class
triangle = Triangle()

# access method inside class
triangle.calculate_area()