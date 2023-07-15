class User:  # User parent or base or super class
    users = 0   #class variable
    def __init__(self,name,pwd):
        self.user_name=name  #instance variable
        self.pwd=pwd
        User.users += 1

    def register(self):
        print('Registered')
        return self       # for method chaining
    def loggin(self):
        print('Loggin')

class Student(User): # student class inherits User class

    def __init__(self, name, pwd,course,fees):
        super().__init__(name, pwd)     #super function is used to acess parent class methods
        self.course=course
        self.fees=fees

    def greet(self):
        print("Hello",self.user_name)

sf1=Student('Ram','1234','cs',25000)
sf1.greet()

sf2=Student('Sam','2543','cs',63000)
sf2.greet()