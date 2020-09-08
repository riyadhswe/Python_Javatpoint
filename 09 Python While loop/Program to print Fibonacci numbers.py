terms = int(input("Enter the terms "))
# first two intial terms
a = 0
b = 1
count = 0

# check if the number of terms is Zero or negative
if (terms <= 0):
    print("Please enter a valid integer")
elif (terms == 1):
    print("Fibonacci sequence upto", limit, ":")
    print(a)
else:
    print("Fibonacci sequence:")
    while (count < terms):
        print(a, end=' ')
        c = a + b
        # updateing values
        a = b
        b = c

    count += 1