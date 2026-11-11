print("lets study range function today ")
'''The range() function can be called with 1, 2, or 3 arguments, using this syntax:
range(start, stop, step)

Call range() With One Argument
The start argument is optional, and if not provided, it defaults to 0
Create a range of numbers from 0 to 9:'''

x1=range(10)
print(x1)
print(len(x1))
print(list(x1))
print(6 in x1)


'''Call range() With Two Arguments
If the range function is called with two arguments, the first argument represents the start value, and the second argument represents the stop value.
range(3, 10) returns a sequence of each number from 3 to 9'''

x2=range(3,10)
print(x2)
print(len(x2))
print(list(x2))
print(6 in x2)


'''
In Python's range() function, the default values are:
start: 0
step: 1
range(3) is equivalent to range(0, 3, 1)
range(3,10) is equivalent to range(3, 10, 1)
'''

x3=range(3,10,2)
print(x3)
print(len(x3))
print(list(x3))
print(6 in x3)