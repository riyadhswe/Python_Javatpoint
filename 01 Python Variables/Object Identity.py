a = 50
b = a
print(id(a))
print(id(b))
# Reassigned variable a
a = 500
print(id(a))  