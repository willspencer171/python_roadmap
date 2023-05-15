# Queues, Stacks, Heaps and Graphs

## Yikes, this took a while! Even though I was following a tutorial :/

---
For this little section, the first in this project, I started from [Python Stacks, Queues, and Priority Queues in Practice](realpython.com/queues-in-python). This was definitely going in at the deep end, but I kind of got to grips with it all down the line.

This tutorial took me through the fundamentals of what a queue is, how it can be modified to create a stack, and what different kinds of deques or heaps or priority queues there are. Lots going on.

Obviously, the first place to start is queues and stacks - FIFO and FILO (modified cos I like pastry) data structures. Relatively simple! In my [code](https://github.com/willspencer171/python_roadmap/tree/master/Data%20Structures/queues.py) you can see that I have a Mixin that I created. all it does is add in a \_\_iter\_\_() method to create a generator that allows a user to iterate through the queue. I've learned that generators are very useful and that the `yield` keyword isn't frightening anymore :)

The last part of the tutorial was a nightmare - purely because of installing [pygraphviz](https://pygraphviz.github.io). I hope the developers know that I don't like them. Anyway, once I finally got that installed, I put queues and stacks to practice. There were some bits and pieces in there that I was just blindly following `[line for line in code]` but the whole thing, once I commented it up, made sense in the scheme of traversals and searches. Now I can tell you that the shortest path from Portsmouth to Edinburgh is:
<center>Portsmouth → Southampton → Winchester → Oxford → Coventry → Birmingham → Stoke-on-Trent → Manchester → Salford → Preston → Lancaster → Carlisle → Edinburgh
</center>

In case you were wondering.

>In all of this, I have learned:
>
> - How to implement a queue, stack, heap and priority queue in Python
>   - Couldn't do it again, mind you
> - What a Mixin is, and how to use one
> - How to battle with pip and a developer that can't quite make their package simple to install
>   - I shouldn't complain though, from everything that I've seen, they've had a hard time doing so
> - How to implement breadth- and depth-first traversals and searches on data
> - That Python can have callback functions similar to those in JavaScript (please don't flame me if this is wildly out of pocket but they correlate in some way in my brain)
>   - And these methods can be declared inside a class that serves no other purpose than to contain these :) (see SearchSortStrat in [graph.py](https://github.com/willspencer171/python_roadmap/tree/master/Data%20Structures/graph.py))
> - Also Dijkstra's shortest path algorithm! Shoutout to my A Level teacher whose voice I can hear that name in!

As always, please feel free to provide **constructive** criticisms by reaching out to me on [Instagram](https://www.instagram.com/will_spencer171) or [LinkedIn](https://www.linkedin.com/in/willspencer171). I'm always learning and people always have opinions so let me hear them!
