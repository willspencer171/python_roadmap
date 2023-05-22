'''
Iterators are a type of object that contains a countable number of values
They can be iterated over

Iterables are objects from which an iterator can be generated

Iterators are what is used in a for or while loop (as well as comprehensions),
not the iterable itself.

if you say:

`for item in my_tuple:`

what you're doing is iterating over each item in the iterator generated from
the my_tuple object

All iterators are iterables - i.e. they have the __iter__() dunder method - 
but not all iterables are iterators - i.e. an iterator must have the __next__() method

iter() can be called on an iterable to convert it to an iterator object

e.g. iter(str) allows you to call next() on the string to get the next character
'''
string = "GFG"
ch_iterator = iter(string)

print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))

# The following code creates a custom iterator class that takes limit as a parameter
# This limit is what is printed *up to* starting from 10
# In other words, Test is a modified version of range where the first number
# is fixed to 10

# An iterable user defined type
class Test:

    # Constructor
    def __init__(self, limit):
        self.limit = limit

    # Creates iterator object
    # Called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self

    # To move to next element. In Python 3,
    # we should replace next with __next__
    def __next__(self):

        # Store current value ofx
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

        # Else increment and return old value
        self.x = x + 1
        return x


# Prints numbers from 10 to 15
for i in Test(15):
    print(i)

# Prints nothing
for i in Test(5):
    print(i)
