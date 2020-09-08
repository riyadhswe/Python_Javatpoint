Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday"}
Days2 = {"Monday", "Tuesday"}
Days3 = {"Monday", "Tuesday", "Friday"}

# Days1 is the superset of Days2 hence it will print true.
print(Days1 > Days2)

# prints false since Days1 is not the subset of Days2
print(Days1 < Days2)

# prints false since Days2 and Days3 are not equivalent
print(Days2 == Days3)