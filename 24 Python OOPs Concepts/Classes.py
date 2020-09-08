class Employee:
    id = "173-35-22487"
    name = "John"
    def display (self):
        print("ID: %s \nName: %s"%(self.id,self.name))
# Creating a emp instance of Employee class
emp = Employee()
emp.display() 