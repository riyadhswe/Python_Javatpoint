# Python delattr() function example
class Student:
    id = 101
    name = "Rohan"
    email = "rohan@abc.com"
    def getinfo(self):
        print(self.id, self.name, self.email)
s = Student()
s.getinfo()
delattr(Student,'email') # Removing attribute
s.getinfo() # error: no attribute 'email' is available