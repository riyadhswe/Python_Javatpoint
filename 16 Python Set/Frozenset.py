Dictionary = {"Name":"John", "Country":"USA", "ID":101}
print(type(Dictionary))
Frozenset = frozenset(Dictionary); #Frozenset will contain the keys of the dictionary
print(type(Frozenset))
for i in Frozenset:
    print(i)    