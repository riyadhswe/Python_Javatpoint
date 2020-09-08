class Details:
    age = 22
    name = "Phill"


details = Details()
print('The age is:', getattr(details, "age"))
print('The age is:', details.age)