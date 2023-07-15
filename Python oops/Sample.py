# base class
class Car:
    
    def start(self):
        print( "I can start and ride now!")
    
    def stop(self):
        print("I can stop now!")

# derived class
class Benz(Car):
    def speed(self):
        print("My speed is 360km/hr !")

# Create object of the Car class
car1 = Benz()

# Calling members of the base class
car1.start()
car1.stop()

# Calling member of the derived class
#benz1=Benz()
car1.speed()