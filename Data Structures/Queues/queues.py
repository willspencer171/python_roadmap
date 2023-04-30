#! python3

# Queues are a linear data structure
# There are FIFO, LIFO, Deque (double-ended) and Priority Queues

# Double-Ended Queue (deque) acts like a combination of a queue and stack 
# - it can be both FIFO and LIFO in a sense
from collections import deque   # Built-in deque class

# Mixin class to provide iterable functions to multiple classes
# Has no __init__ definition so it cannot be initialised as an object
# Can only be inherited so attributes of self have no context until the class
# is MixedIn (inherited)
class IterableMixin:
    # Queue can report its length
    def __len__(self):
        return len(self._elements)

    # Queue is now iterable as well
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()
            # This is a form of lazy evaluation - delays the evaluation of an expression
            # until it is needed (i.e. every time it's iterated over)


# Custom queue that simply wraps a deque from the collections module, and 
# then adds enqueue (add) and dequeue (remove) methods
# This is a simple FIFO queue, since the enqueue adds to the tail, and dequeue
# pops from the head
class Queue(IterableMixin):
    def __init__(self, *elements):
        # Etymology - _elements has prefixed _ to denote private variable
        self._elements = deque(elements)

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()
    
# To make a stack, we inherit the above Queue class, 
# then override the dequeue method to pop from the tail
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

# Priority queues using a heap to represent
# A heap is a data structure similar to a list that maintains relationships between
# elements. This doesn't mean it's always sorted, just that it knows how to relate
# elements to one another
# In python, heaps are min-heaps which means they sort lowest to highest
from heapq import heappop, heappush, heapify
from itertools import count

class PriorityQueue(IterableMixin):
    # initialise list of elements
    def __init__(self):
        self._elements = []
        # Count will initialise a generator that can be incremented
        # every time an element is pushed to the queue
        self._count = count()
    
    # push onto heap and insert into current list, based on priority
    # using -priority means that highest priority items are first to be popped
    # if items with the same priority are found, the next comparator
    def enqueue_with_priority(self, priority, value):
        new_el = (-priority, next(self._count), value)
        heappush(self._elements, new_el)
    
    # pop the first item, opposite to pop()
    def dequeue(self):
        # [1] used to return just the value, rather than priority level and value
        return heappop(self._elements)[-1]

from typing import Any
from dataclasses import dataclass

@dataclass(order=True)
class Element:
    priority: float
    count: int
    value: Any

"""
The main difference between this and the priority queue
is that this is mutable - we can see and modify priority
However, the priority queue was based on a NamedTuple and
Tuples are inherently immutable
"""
class MutableMinHeap(IterableMixin):
    def __init__(self):
        super().__init__()
        self._elements_by_value = {}
        self._elements = []
        self._counter = count()
    
    def __setitem__(self, unique_value, priority):
        if unique_value in self._elements_by_value:
            self._elements_by_value[unique_value].priority = priority
            heapify(self._elements)
        else:
            element = Element(priority, next(self._counter), unique_value)
            self._elements_by_value[unique_value] = element
            heappush(self._elements, element)

    def __getitem__(self, unique_value):
        return self._elements_by_value[unique_value].priority

    def dequeue(self):
        return heappop(self._elements).value
