class User:  # User parent or base or super class
    users = 0   #class variable
    def __init__(self,name,pwd):
        self.user_name=name  #instance variable
        self.pwd=pwd
        User.users += 1

    def register(self):
        print('Registered ' + self.user_name)
        return self       # for method chaining
    def loggin(self):
        print('Loggin ' + self.user_name)

user1=User('Ram','1234')
user2=User('Sam','12&%4')
user3=User('Ravi','12@54')

user1.register().loggin()
user2.loggin()
print(user1.user_name,user1.pwd)
print(user2.user_name,user2.pwd)
print(User.users)