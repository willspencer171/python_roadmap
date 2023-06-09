'''
List comprehesions are nice, easy ways of creating a list from a list

It can be used to replace both map and reduce if needed
'''

# List comps have the following structure:
iterable = "hello"
output = [expression for expression in iterable if True]
print(output)

# You can realistically have as many ifs and fors as you like after the initial for
output = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(output)

# List comprehensions are elegant one liners that can reduce several lines of
# looping into a single expression

output = [round(item/17, 2) for item in [1,3,5,67,6,7654]]
print(output)

'''
Can also do dictionary comprehensions
'''

# You can manipulate both k and v or one or neither
output = {k+1: v**2 for k, v in enumerate([1,2,3,4,5,6,7,8,9]) if not v & 1}
print(output)

'''
Generators and Generator expressions

A generator is function that yields a value upon iteration

A generator expression is an expression (similar to list comprehension)
that is stored in a variable as a generator object
'''

# Generator function
def gen_func(num):
    for n in range(1, num+1):
        yield n**2

for square in gen_func(5):
    print(square)

# Same thing, generator expression
squares = (n**2 for n in range(1, 6))

for square in squares:
    print(square)

# So what's the point? I can do the same thing with list comprehension
'''
A generator is different to a list - a value is generated on each iteration
rather than the whole list being stored in memory

For example, the generator expression above has one memory location,
but the list, output, stores each of its values in memory locations.

So a list of 5 square numbers would take up 5 times the number of memory locations
Nominal on small scales, but if you have a lot of pieces of data, this can get quite
cumbersome and exhaustive.

The only tradeoff is that once a generator has been iterated over, it is exhausted
and needs to be declared again
'''
