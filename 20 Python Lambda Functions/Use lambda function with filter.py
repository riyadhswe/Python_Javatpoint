#program to filter out the tuple which contains odd numbers
lst = (10,22,37,41,100,123,29)
oddlist = tuple(filter(lambda x:(x%3 == 0),lst)) # the tuple contains all the items of the tuple for which the lambda function evaluates to true
print(oddlist)    