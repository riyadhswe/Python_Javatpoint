class Employee:
    id = 10
    name = "John"

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))
        # Creating a emp instance of Employee class


emp = Employee()

# Deleting the property of object
del emp.id
# Deleting the object itself
del emp
emp.display()