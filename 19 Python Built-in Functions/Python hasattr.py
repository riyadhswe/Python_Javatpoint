class Employee:
    age = 21
    name = 'Phill'


employee = Employee()

print('Employee has age?:', hasattr(employee, 'age'))
print('Employee has salary?:', hasattr(employee, 'salary'))