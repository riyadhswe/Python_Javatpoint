# The function simple_interest(p, t, r) is called with the keyword arguments.
def simple_interest(p, t, r):
    return (p * t * r) / 100


# doesn't find the exact match of the name of the arguments (keywords)
print("Simple Interest: ", simple_interest(time=10, rate=10, principle=1900))