from queues import *
from graph import *

# Read data from roadmap.dot and convert each node into a City object
nodes, graph = load_graph("Data Structures/roadmap.dot", City.from_dict)

""" print(nodes["london"])
print(graph) """

# This will access the neighbours and weights connecting to London
# and print them
# Needed square bracket notation to access two things
# The two things are key and value with value being a named tuple
# containing both 'distance' and 'label'. These are the same value in this file
""" for neighbor, weights in graph[nodes["london"]].items():
    print(weights["distance"], neighbor.name) """

# Sort by helper function
# returns a sorted dictionary, sorted on a given strategy method
def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

# and distance strategy 
# (this works like reduce does, in that this would be the callback)
def by_distance(weights):
    return float(weights["distance"])

# The :>3 in the f-string {} says "right aligned to 3 spaces"
# https://docs.python.org/3/library/string.html#:~:text=Aligning%20the%20text%20and%20specifying%20a%20width%3A
""" for neighbour, weights in sort_by(graph[nodes["london"]], by_distance):
    print(f"{weights['distance']:>3} miles, {neighbour.name}") """
# Let's keep this in mind in future - f-strings can be manipulated
# more than you think

# This traverses the graph breadth-first starting from Edinburgh
""" for city in breadth_first_traverse(graph, nodes["portsmouth"]):
    print(city.name) """

# The predicate is simply a function that returns a boolean
# This can be a lambda if you so wish, similar to callback
""" city = breadth_first_search(graph, nodes["ripon"], 
                            lambda city: city.lat <= 54,
                            SearchSortStrat.city_name
)
print(city.name)
for city in breadth_first_traverse(graph, nodes["inverness"],
                                   SearchSortStrat.city_name):
    print(f"Founding Year: {round(city.year, 2):>4} --- {city.name}")
 """

print("Shortest path bfs".center(30, "="))
print(" → ".join(city.name for city in shortest_path_bfs(graph,
                                                         nodes["portsmouth"],
                                                         nodes["york"],
                                                         SearchSortStrat.founding_year_inv)))

print(is_connected(graph, nodes["glasgow"], nodes["belfast"]))

""" Depth-First Traversal """
print("Depth-First traverse".center(30, "="))
for city in depth_first_traverse(graph, nodes["edinburgh"],
                                 SearchSortStrat.latitude):
    print(f"{round(city.lat, 2):^5} --- {city.name}")

city = rec_depth_first_traverse(graph, nodes["portsmouth"],
              lambda city: city.lat >= 54)
print("Search result - depth-first (recursive)")
print(round(city.lat, 2), city.name, sep=" --- ")

""" THE THING ABOUT THESE """
""" 
We can't use a stack or a queue to perform a Dijkstra's Search
to determine the shortest path dependent on weights

We can however, use a priority queue to do this
"""

print("\n"*3, " Dijkstra ".center(30, "="))
route = " → ".join(city.name for city in dijkstra_shortest_path(graph, nodes["portsmouth"],
                                   nodes["edinburgh"],
                                   lambda weights: float(weights["distance"])))

print(route)
