# Object-Oriented Programming (OOP)

## 'Lecture Notes' from [Beginner Crash Course](https://www.youtube.com/watch?v=-pEs-Bss8Wc) YouTube Video

> ### Contents
>
>- [Creating Classes](#creating-classes)
>- [Functions Inside Classes](#functions-inside-classes)
>- [Inheritance](#inheritance)
>- [Encapsulation](#encapsulation)
>- [Properties](#properties-get--set)

### The 4 Principles of OOP

- Inheritance
- Polymorphism
- Encapsulation
- Abstraction

## Creating Classes

In Python (and pretty much most other programming languages) we have data structures that hold information. Built-in data structures like lists are good for holding data:

`my_list = [1, "two", 9/3]`

Great, we have a list that holds information. However, if we want to create, for example, a profile of a worker, this becomes cumbersome once we find that we need more than one (maybe you work at a large company with more than 1 person)

```python
# this is a person, with name, age, salary, and job title
worker1 = ["will spencer", 22, 30000, "Software Engineer"]
worker2 = ["greg davies", 55, 50000, "School Teacher"]
```

We can see how we have the same structure for each case, with each bit of data having a specified meaning. This isn't any good since we'd need to access each piece of information using a list index. This can lead to problems further on where data is missing - if the age of `greg davies` is missing, every index after that point gets shifted by one place.

What we want is to be able to access information about an object using a named property. This *can* be done using a dictionary, but each one would need to be set up separately, rather than programmatically, which would be easier

### Introducing Classes

Classes are essentially templates or blueprints for a specific *type* of object, from which we can create *instances*. Say we want to create our famous Will and Greg people again. We can create them using a class in Python:

```python
class Person:
    # class attribute
    is_human = True
    
    def __init__(self, name, age, salary, job_title):
        # instance attributes
        self.name = name
        self.age = age
        self.salary = salary
        self.job_title = job_title

# Now when we want to make our characters, we can do the following:
will = Person("Will Spencer", 22, "M", "Software Engineer")
greg = Person("Greg Davies", 55, "M", "School Teacher")
```

Now, we can access the different properties of each object thusly:

```python
will.name       # 'Will Spencer'
greg.job_title  # 'School Teacher'
```

`will` and `greg` are both *instances* of the class `Person`, meaning they are objects of type `Person`. `__init__()` is a method that is used to initialise an object. Frankly, you can do just about anything in this method, but it is typically used for creating *instance attributes*. Variables declared outside of the scope of `self` are known as class variables, and they are values shared between every instance of a class:

```python
Person.is_human     # True
will.is_human       # True
```

If either of these types of variable are updated, they are updated across the scope i.e. updating an instance variable changes the value for *that* instance, and updating a class variable updates it for *all* instances.

## Functions inside classes

Classes can contain functions. This is a really good thing that sets aside classes from other data structures that we could use to represent an object. For example, in the list representation we used earlier, we couldn't define a function in that, it just wouldn't make sense. We could however store a function in the list. Huzzah! We have a workaround!

```python
def code():
    print("I am coding")

will = ["will spencer", 22, 30000, "Software engineer", code]
greg = ["greg davies", 55, 50000, "School Teacher", code]
```

But wait... Greg Davies can code? That magnificent beast! Perhaps there are teachers out there who can code (I should hope so since it's on the curriculum), but we don't necessarily want our `greg` to be able to code when we run:

```python
greg[-1]()
```

We want to minimise our scope such that *only* software engineers can code. We can do this by adding it to a `SoftwareEngineer` class:

```python
# ...
class SoftwareEngineer:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    # self needs to be passed as a parameter
    def code(self):
        print(self.name, "is coding...")

# I got a promotion since the last run
will = SoftwareEngineer("Will Spencer", 22, 60000)

# the object gets passed as self, removing the need to pass it in code()
will.code()     # 'Will Spencer is coding...'
greg.code()     # Throws an error - 'code is not a property of Person'

# Side note, self is an arbitrary name, just convention that we call it self
# The same way that cls is the conventional name for a classmethod's first parameter
```

So there we go, we've added a method whose scope is limited only to the `SoftwareEngineer` class. The only problem here is that I am no longer a Person - I've had my identity as a human stripped just to become a Software Engineer and earn a better salary :')

Why can't I be both? I can! I just have to inherit my `Person`ness as I become a `SoftwareEngineer`. More to [follow](#inheritance)

There are also some methods, similar to `__init__()` called dunder (double under) methods. These are special, reserved method names used in class definitions to apply special functionality to a class. For a quick example, I'll show `__str__()` and `__repr__()` (which are not the same, but similar)

```python
class SoftwareEngineer:
    # ...
    def __str__(self):
        return f"name: {self.name},\nage: {self.age},\n salary: {self.salary}"
    
    def __repr__(self):
        return f"Object <SoftwareEngineer> at {id(self)}

# ...
str(will)       # name: Will Spencer,
                # age: 22,
                # salary: 60000
print(will)     # name: Will Spencer,
                # age: 22,
                # salary: 60000
repr(will)      # Object <SoftwareEngineer> at 0x140234866093264
```

The main difference between `__str__()` and `__repr__()` is that the string method is designed to return a human-legible representation of the object, whereas the `repr()` returns an *unambiguous* representation of the object (using the object ID in this instance). The `repr()` default representation is pretty good as-is, but the option is there to manipulate as I have.

I have another file dedicated to dunder methods somewhere around here.

Another thing about methods in classes is making the scope of the function for both classes *and* instances, without requiring that the first parameter of the method be `self` or `cls`.

In the case of `Person`, I could write a function that just prints "is doing something":

```python
class Person:
    # ...
    def doing_something():
        print("I'm a person, doing something")
```

The problem with this is that this requires a positional argument, `self` to specify whether the function is in use by the class or the instance. We don't want that, but we don't want to cast out our method to the nether realms of main(). This can be done using the `@staticmethod` decorator:

```python
class Person:
    # ...
    @staticmethod
    def doing_something():
        print("I'm a person, doing something")
```

And it's not required anymore that an argument be passed to the function and can be called by both the class and the instance:

```python
Person.doing_something()    # I'm a person, doing something
greg.doing_something()      # I'm a person, doing something
```

>You've made it about halfway through this README, I'm so proud of you, keep going! I talk about whales in the next section!
>
>Thanks for reading as far as you have, I really do appreciate it so I'm going to give you a slice of cake, just for you :cake::plate_with_cutlery:

## Inheritance

Oh look, it's that thing I was talking about in the last section! Thanks to everyone's favourite Austrian Monk/Biologist/Pea breeder Gregor Mendel, inheritance is a pretty well-mapped out concept. Inheritance is the method by which traits from a parent are passed to a child. Important choice of words there. In terms of what we're talking about, inheritance is the ability to create a class (child) that derives properties from another class (parent). A good way of looking at this is through the lens of taxonomy - the categorisation and ordering of the natural world.

Say we have a blue whale (*Balaenoptera musculus*) and a Bryd's whale (*Balaenoptera edeni*). We can see that these are both species of the *Balaenoptera* genus. This means they share properties unique to *Balaenoptera*, but have unique properties of their own:

```python
class Balaenoptera:
    alias = "Rorqual Whales"
    latin_genus_name = "Balaenoptera"
    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size
    
    def swim(self):
        print(f"{self.name} is swimming")

class musculus(Balaenoptera):
    alias = "Blue Whale"
    latin_name = super().latin_genus_name + " musculus"
    
    def __init__(self, name, age, size):
        super().__init__(name, age, size)

class edeni(Balaenoptera):
    alias = "Bryd's Whale"
    latin_name = super().latin_genus_name + " edeni"

    def __init__(self, name, age, size):
        super().__init__(name, age, size)
    

blue_whale = musculus("Sheila", 13, 15)
bryds_whale = edeni("Barbara", 10, 10)
rorqual_whale = Balaenoptera("Unknown Species 'George'", 7, 5)

blue_whale.alias                # Blue Whale
blue_whale.latin_genus_name     # Balaenoptera
blue_whale.latin_name           # Balaenoptera musculus
musculus.latin_name             # Balaenoptera musculus

bryds_whale.name                # Barbara
edeni.latin_genus_name          # Balaenoptera
bryds_whale.swim()              # Barbara is swimming

rorqual_whale.name              # Unknown Species 'George'
rorqual_whale.latin_name        # Throws error - no property called 'latin_name'

Balaenoptera.alias              # Rorqual Whales
Balaenoptera.latin_name         # Throws error - no property called 'latin_name'
```

Beautiful. This shows how class attributes can be inherited from parent the class `Balaenoptera` and different properties can be overridden by child classes. Here, we can also create an instance of a Rorqual Whale that doesn't yet have a species identifier (either because it isn't recognised or is a new species) and it is still a valid object.

The `super()` special method is used to retrieve information from the parent class and use it in the child class. We use `super().__init__()` to retrieve the parent's init method and use that in the child's one too. This reduces the amount of repeated code since you're accessing it from the parent (remember, keep your computer DRY).

Class instances and methods are inherited from the parent, and can be overridden and used in the child class.

### Polymorphism

From Greek ('many shapes'), polymorphism is the ability of a child class to behave like it's parent class. In the case of what we laid out above, we can call `swim()` on any child object derived from the Rorqual Whales regardless of which species it is:

```python
for whale in [blue_whale, bryds_whale, rorqual_whale]:
    whale.swim()

''' output:
Sheila is swimming
Barbara is swimming
Unknown Species 'George' is swimming
'''
```

This can be done because each of the whales has the `swim()` method, meaning the Blue and Bryd's whales can `swim()`, exactly the same way that the unknown Balaenopterid will (this is a simplification, there is of course lots of maths that is involved with the way whales swim based on size and experience but still, the concept holds)

## Encapsulation

Encapsulation is the idea that we are wrapping information and methods that work on our information within the class unit (aside from keeping everything tidy and under one roof, this provides security and data consistency)

I mention security and consistency because if we encapsulate our data, we can make certain things accessible only within the class and its methods, rather than directly accessing them from outside the class or via instances. In Python, this is typically denoted by putting a single underscore before the name of an attribute:

```python
# Let's go back to the first example of people
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Some mystery, protected variable
        self._salary = None
```

What I've done here is I've created a class with the attributes `name`, `age`, and `_salary`. Two of them are given values when an instance of the class is initialised, the other is not yet assigned a value and is defaulted to `None` (could be any value). While yes, it is possible to access the `_salary` attribute from outside the class, we say "please don't, I even marked it for you so don't touch". So that's a big no-no.

Because we shun people if they directly access protected variables, we need a way for them to still manipulate the data stored there indirectly:

```python
class Person:
    # ...
    def get_salary(self):
        return self._salary
    def set_salary(self, value):
        self._salary = value
```

Because we have methods here, this opens up a world of possibilities for protecting our variables! We can say:

```python
# I'm going to change _salary to __salary here, because 
# this is how we define a private variable - can't access 
# it from outside even if you try
def set_salary(self, value):
    if value < 15000:
        value = 15000       # We don't encourage poor pay here, but allow it anyway
    self.__salary = value
```

And this will set the salary value, without directly accessing the salary attribute, as well as impose checks on the value that someone is trying to input.

This also allows us to do things like use other internal attributes to affect how, say, salary is set, depending on an employee's performance. All of the things we can do with normal functions and attributes, we can do with protected ones. No need for a decorator or anything, just stick __ in front of it.

At this point I think I'm a little confused, but here's my understanding:

>Encapsulation unifies a bunch of things (attributes and methods) under one umbrella (the object).
>
>Next, the video I'm following says "so yeah this is abstraction" - bruh you just said it was encapsulation?
>
>Abstraction is the process of hiding unnecessary code from a user (i.e. protecting it from the user and the user from it). We are metaphorically placing the hood over the code that is running 'under the hood' when certain user-accessible functionality is run.

## Properties

This is what you'll sometimes see on an object whose attributes you are trying to reach. A property looks a lot like an attribute, but it's actually a getter function with a `@property` decorator. Have a look at my [Hash Table](https://vscode.dev/github/willspencer171/python_roadmap/blob/master/Data%20Structures/Hash%20Tables/hashtable_sep_chain.py#L179) file, which includes a few properties.

One thing that I haven't used before but is interesting is setting and deleting properties using decorators:

```python
class Person:
    def __init__(self):
        self.__salary = None
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        self.__salary = value
    
    @salary.deleter
    def salary(self):
        self.__salary = None
```

Once a getter function is designated as a property using the `@property` decorator, the `@property.setter` and `@property.deleter` decorators can be used. This allows for the following notation:

```python
# ...
will = Person()
will.salary         # None
will.salary = 25000
will.salary         # 25000
del will.salary
will.salary         # None
```

What's really good about using properties is that the `__salary` attribute is so far abstracted that we can use the name `salary` to access it as if it were the name of the attribute instead of `__salary`. No more `will.get_salary()`

Now, I'm both at the end of the video lecture and my wit's end SO I'm gonna sign this off and say my usual thing

THANK YOU SO MUCH for making it to the end of this absolute drivel. You've done well to make it this far and I'm proud of you for it. I know it wasn't easy.

As always, if you want to talk more about what's going on on these pages, send me a message on [Instagram](https://www.instagram.com/will_spencer171) or [LinkedIn](https://www.linkedin.com/in/willspencer171) and let me know if you enjoyed your cake!
