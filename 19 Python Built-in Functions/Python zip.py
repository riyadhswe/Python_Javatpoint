numList = [4, 5, 6]
strList = ['four', 'five', 'six']

# No iterables are passed
result = zip()

# Converting itertor to list
resultList = list(result)
print(resultList)

# Two iterables are passed  
result = zip(numList, strList)

# Converting itertor to set
resultSet = set(result)
print(resultSet)