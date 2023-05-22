# Advanced Topics

## Some interesting topics in here, not as in-depth as some of my others so far - so what's in this one?

First, I'll just link the other folders so you know they're there to read if you want, but they each have their own READMEs to go through :)

>- [Object Oriented Programming (OOP)](https://github.com/willspencer171/python_roadmap/tree/master/Advanced%20Topics/OOP)
>- [Modules](https://github.com/willspencer171/python_roadmap/tree/master/Advanced%20Topics/PyModules)

I've got some smaller topics in here that were next on my to-do list according to the [Roadmap](https://roadmap.sh/python). The few that I'll cover in this README are the following:

- Decorators
- Iterators
- Anonymous (lambda) Functions
- Regular Expressions

Within their own rights, these are interesting topics with a lot of explorable depth if you know where to look (and/or have the effort).

## [Decorators](https://github.com/willspencer171/python_roadmap/tree/master/Advanced%20Topics/decorators.py)

These are functions that are used to 'tack on' functionality to other functions without affecting the structure of your newly-defined functions. The way I like to think of them is that they're similar to mixins but for functions and methods, rather than classes and objects.

At first, I think this was the toughest to wrap my head around - the basic structure of a decorator is relatively simple, but I struggled to find relevant use cases for making custom decorators. Obviously, I do see that a lot of other decorators from other modules and even built-ins are very useful (take `@classmethod` or `@property` for example). They have their place, but I have yet to find where that is in my own usage.
>
>- These are good for keeping your code clean and DRY (don't repeat yourself)
>
>- Can be used to limit the scope of different functions and protect information from being passed around or returned to the wrong places
>
>- Is useful for adding functionality to an existing function without modifying the function itself

Overall, not the most enjoyable topic but a topic that needs covering and understanding

## [Iterators](https://github.com/willspencer171/python_roadmap/tree/master/Advanced%20Topics/iterators.py)

Iterators are powerful and compact. They are an object that has a countable amount of things stored inside, and can be iterated through using the builtin `__iter__` method. Curiously, iterables also use this method, but the one thing that sets them aside is the `__next__` function. This allows the iterator object to be manually iterated over in a loop, or passed as an argument to the `next()` function.

Built-in iterables such as strings and lists can be converted to their iterator counterpart by being passed through the `iter()` function. This means that each item stored in the iterable can be accessed in order.

>- I didn't really learn much from writing the code I did in the file, but I think that's okay
>- What I do know that I didn't, however, is that depending on the way you define `__iter__` and `__next__`, you can get wildly different functionality without having to run if statements and the like. It makes sense now that I'm typing it out but I didn't really think of it before. Makes for less general-purpose objects

## [Regex](https://github.com/willspencer171/python_roadmap/tree/master/Advanced%20Topics/regex.py)

Regex (regular expressions) has long evaded me. Every time I've ever seen a regular expression pattern on my screen I've died a little inside (maybe I just need to change my font). However, with the number of cheat sheets I've found and having had a bit of practice, Regex isn't so daunting as much as it is helpful. Pattern matching makes for quick, consistent coding that is legible and modular. We like.

I've been practising Regex using [RegexOne](https://regexone.com/) since I don't really have a lot of example data I can draw experience from, and it's really helped! Of course, reading the [Python Docs](https://docs.python.org/3/library/re.html) on the `re` module is good as well so I can get into the nitty gritty of actual syntax.

>- Regex is not a scary thing anymore! First time I saw it way back in college I hated it because nobody taught me how to read it and nobody taught me what any of it meant. Not thanking Rob for that one
>
>- I also don't feel I need to use ChatGPT straight off the bat to come to a good regex pattern that does what I need it to do, which is nice.
>
>- Patterns are what makes up language, as well as numbers, as well as all data structures. If some data doesn't have a pattern to match it, there's something wrong with the data and it needs restructuring

## [Lambda](https://github.com/willspencer171/python_roadmap/tree/master/Advanced%20Topics/lambdas.py)

The anonymous function. Very useful for if you only need it once or twice. Is lightweight, is cool. Will fit into any spot that a whole, fully structured and defined function will do. HOWEVER, the main caveat is that it is only really any good for one expression.

But that's okay, cos at least this way I'm not making the space complexity of any algorithm worse since there isn't any storage going on - variables go in, variables come out; function gone.

>- A really useful feature that allows for single-line, single-use functions
>
>- Problem is that it can reduce readability of code and also reproducibility since the function isn't being used anywhere else, even if it does get repeated sometimes
>   - In which case, you're better off just using a `def` function
>

Overall, I enjoy lambdas. Since they can be used in lieu of named functions, they can be put into other methods like filter, reduce and map. This makes it powerful without overcomplicating your code. After all, if you need readability, just indent and newline your code properly :)

As always, thanks for reading my READMEs, I hope you had fun like I did writing it :') you're more than welcome to stick around, stay a while and maybe have a cup of tea (bring your own kettle, mugs, tea. milk and water). I'm always happy to have a chat about the stuff I'm doing since it keeps me motivated and curious about what's going on :) as usual you can find me on [Instagram](https://www.instagram.com/will_spencer171) or [LinkedIn](https://www.linkedin.com/in/willspencer171)
