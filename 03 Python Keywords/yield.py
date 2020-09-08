def fun_Generator():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in fun_Generator():
    print(value) 