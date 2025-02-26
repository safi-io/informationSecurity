"""
Lists are used to store multiple items in a single variable.
"""

data = ["safi", 20, 5.10, True]
data.append("khan")

print( data )
print(data[0])
print(len(data))
print(type(data[3]))

numbers = [100,2,3,90,5,6,]
numbers.sort(reverse=True)

print(numbers)
numbers.sort()
print(numbers)