from typing import NamedTuple
from collections import deque
import networkx as nx
from queues import *

class City(NamedTuple):
    name: str
    country: str
    year: int
    lat: float
    long: float

    # This is a Decorator - it adds function to a method without
    # changing the structure of it. They wrap the following
    # method with predefined function. Like inheriting a method
    # from a method, rather than a class from a class
    @classmethod
    def from_dict(cls, attrs):
        return cls(
            name=attrs["xlabel"],
            country=attrs["country"],
            year=int(attrs["year"]),
            lat=float(attrs["latitude"]),
            long=float(attrs["longitude"]),
        )
    # from_dict() will be used to convert a dictionary
    # to a City object

"""
A NamedTuple is inherently hashable i.e. no two values
are the same and therefore can be hashed (affected to be random
via a single algorithm)
It is also comparable which is useful for 
traversing a graph of Citys
"""
# Node factory is a function. In this case, it'll be City.from_dict
def load_graph(filename, node_factory):
    graph = nx.nx_agraph.read_dot(filename)
    nodes = {
        # Dictionary comprehension, just a really much nicer
        # way to write it
        name: node_factory(attributes) 
        for name, attributes in graph.nodes(data=True)
    }
    # Returns all the nodes generated above, from the file
    # then generates a graph from these nodes and returns that too
    return nodes, nx.Graph(
        # This is a tuple or set comp
        (nodes[name1], nodes[name2], weights)
        for name1, name2, weights in graph.edges(data=True)
    )

# Gonna make a method for a breadth-first traversal, followed by
# a bf search method
def breadth_first_traverse(graph, source, order_by=None):
    queue = Queue(source)
    visited = {source}
    # This works because our queue is iterable and dequeues
    # when iterated
    for node in queue:
        # This makes more sense to me ngl
        yield node
        neighbors = list(graph.neighbors(node))
        if order_by:
            neighbors.sort(key=order_by)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)

# we can iterate through the bft because of the yield statement

# Will just return the first node that yields a truthy predicate statement
def breadth_first_search(graph, source, predicate, order_by=None):
    return search(breadth_first_traverse, graph, source, predicate, order_by)

# these startegies are used to order the nieghbours of a given node
# It can also be used to sort a dictionary of nodes as key=fn
class SearchSortStrat:
    # prioritise lower -> higher
    def latitude(neighbor):
        return neighbor.lat
    # prioritise higher -> lower
    def latitude_inv(neighbor):
        return -neighbor.lat

    def longitude(neighbor):
        return neighbor.long
    def longitude_inv(neighbor):
        return -neighbor.long

    def founding_year(neighbor):
        return neighbor.year
    def founding_year_inv(neighbor):
        return -neighbor.year

    def city_name(neighbor):
        return neighbor.name

# Modified breadth-first search that builds a list of previous nodes
# that make up the path
def shortest_path_bfs(graph, source, destination, order_by=None):
    queue = Queue(source)
    visited = {source}
    previous = {}
    # node is the current, starts off as just the source,
    # and grows with each iteration of the second for loop
    # so that that node is checked later
    for node in queue:
        neighbors = list(graph.neighbors(node))
        if order_by:
            neighbors.sort(key=order_by)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
                # adds dict key with value of current node
                # the neighbour is the previous
                previous[neighbor] = node
                if neighbor == destination:
                    # retrace will return the path as a list
                    return retrace(previous, source, destination)

def retrace(previous: dict, source, destination):
    path = deque()
    current = destination
    while current != source:
        path.appendleft(current)
        # This is smart, the value of the current key is the
        # previous node
        current = previous.get(current)
        if current is None: # .get() returns none if no return
            return None # i.e. There are no previous nodes
        
    path.appendleft(source)
    return list(path)

# checks if there is a connection between two sites
def is_connected(graph, source, destination):
    return shortest_path_bfs(graph, source, destination) is not None


""" Depth-First Traversal and Search """


def depth_first_traverse(graph, source, order_by=None):
    stack = Stack(source)
    # Instead of adding source, just initialise an empty set
    visited = set() # we need to be able to revisit the source and its neighbours
    for node in stack:
        # Check earlier if node in visited
        if node not in visited:
            yield node
            visited.add(node)
            neighbors = list(graph.neighbors(node))
            if order_by:
                neighbors.sort(key=order_by)
            # Reverse to account for enqueue direction of stack
            for neighbor in reversed(neighbors):
                stack.enqueue(neighbor)

"""
This uses a stack data structure rather than a queue
Because of this, we can actually just use the python call stack
by making a recursive function
This means we don't actually have to maintain our own stack data
structure since python fundamentally has one built in
"""
def recursive_depth_first_traverse(graph, source, order_by=None):
    visited = set()

    def visit(node):
        yield node
        visited.add(node)
        neighbors = list(graph.neighbors(node))
        if order_by:
            neighbors.sort(key=order_by)
        for neighbor in neighbors:
            if neighbor not in visited:
                # yield from opens a two way gate into 
                # the generator, visit and gets the value
                # that it yields
                # https://stackoverflow.com/questions/9708902/in-practice-what-are-the-main-uses-for-the-yield-from-syntax-in-python-3-3
                yield from visit(neighbor)
    
    # Trigger recursion of visit
    # The function is passed to the call stack on each call,
    # and the value of it is popped on every return
    return visit(source)

"""
Now that we have both depth first and breadth first traversals,
We can create a template function to search(), specifying either
depth or breadth first
"""
def depth_first_search(graph, source, predicate, order_by=None):
    return search(depth_first_traverse, graph, source, predicate, order_by)

def rec_depth_first_traverse(graph, source, predicate, order_by=None):
    return search(recursive_depth_first_traverse, graph, source, predicate, order_by)

def search(traverse, graph, source, predicate, order_by=None):
    for node in traverse(graph, source, order_by):
        if predicate(node):
            return node

# another function comes in here for the Dijkstra algo
from math import inf as infinity

def dijkstra_shortest_path(graph, source, destination, weight_factory):
    previous = {}
    visited = set()

    unvisited = MutableMinHeap()
    for node in graph.nodes:
        # default all nodes as inaccessible
        unvisited[node] = infinity
    # default source as 0 distance
    unvisited[source] = 0

    for node in unvisited:
        visited.add(node)
        for neighbor, weights in graph[node].items():
            weight = weight_factory(weights)
            new_distance = unvisited[node] + weight
            if new_distance < unvisited[neighbor]:
                unvisited[neighbor] = new_distance
                previous[neighbor] = node

    return retrace(previous, source, destination)
