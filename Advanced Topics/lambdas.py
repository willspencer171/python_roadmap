'''
A lambda function is anonymous. This means it can be created and run without being stored 
or named (keeping space complexity to a minimum)

They work exactly the same way that functions do, but usually only work over the course of a single line
'''

# Let's start simple
a_string = "FuzzySand747367"

rev_upper = lambda x: x.upper()[::-1]

# Nicely, this reverses the string and converts to uppercase
print(rev_upper(a_string))

# Can also be used in a map() method
# Alternate uppercase based on index
updated = list(map(lambda x: x[1].upper() if x[0] & 1 else x[1].lower(), enumerate(a_string)))
print("".join(updated))

# Let's do with a list comp
# Interestingly, the lambda needs to be called in order to access it
# It doesn't run it then store it, it stores the lambda function so it can be run later
list_comp = [lambda arg=x: arg**2 for x in range(0, 9)]
for i in list_comp:
    print(i())

# Let's try with filter and reduce

from functools import reduce

list_to_work = list(range(1, 20))

filtered = set(filter(lambda x: not x & 1, list_to_work))
factorial = reduce(lambda a, b: a * b, list_to_work)
summed = reduce(lambda a, b: a + b, list_to_work)

print(filtered)
print(factorial)
print(summed)
