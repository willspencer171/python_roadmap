#! python3
from collections import Counter

def distribute(items, num_containers, hash_function=hash):
    return Counter([hash_function(item) % num_containers for item in items])

def plot(histogram):
    for key in sorted(histogram):
        count = histogram[key]
        padding = (max(histogram.values()) - count) * " "
        print(f"{key:3} {'■' * count}{padding} ({count})")

""" 
1. Create an empty hash table
2. Insert a key-value pair to the hash table
3. Delete a key-value pair from the hash table
4. Find a value by key in the hash table
5. Update the value associated with an existing key
6. Check if the hash table has a given key
"""
"""
1. Create a hash table from a Python dictionary
2. Create a shallow copy of an existing hash table
3. Return a default value if the corresponding key is not found
4. Report the number of key-value pairs stored in the hash table
5. Return the keys, values, and key-value pairs
6. Make the hash table iterable
7. Make the hash table comparable by using the equality test operator
8. Show a textual representation of the hash table
"""
from typing import NamedTuple, Any
from collections import deque

class Pair(NamedTuple):
    key: Any
    value: Any

class HashTable:
    # Initialise class instance
    # load factor threshold is optional, means "at what percentage
    # would you like to resize the table?"
    def __init__(self, capacity=8, load_factor_threshold=0.6):
        if type(capacity) != int:
            raise TypeError("Hash Table size must be an integer")
        if capacity < 1:
            raise ValueError("Capacity of hash table must be positive")
        self._buckets = [deque() for _ in range(capacity)]
        self._load_factor_threshold = load_factor_threshold
    
    # Return length of instance
    # use len()
    def __len__(self):
        return len(self.items)
    
    # iterate through and yield iterable
    # use loops (while / for)
    def __iter__(self):
        yield from self.keys
    
    # create / update item
    # square bracket notation
    def __setitem__(self, key, value):
        if self.load_factor >= self._load_factor_threshold:
            self._resize_and_rehash()
        
        bucket = self._buckets[self._index(key)]
        for index, item in enumerate(bucket):
            if item.key == key:
                bucket[index] = Pair(key, value)
                break
        else:
            bucket.append(Pair(key, value))
    
    # retrieve item if exists
    # can use square bracket notation
    def __getitem__(self, key):
        bucket = self._buckets[self._index(key)]
        for item in bucket:
            if item.key == key:
                return item.value
        raise KeyError(key)
    
    # Check if key exists
    # can use 'in' keyword
    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True
    
    # be able to use the del keyword
    def __delitem__(self, key):
        bucket = self._buckets[self._index(key)]
        for index, item in enumerate(bucket):
            if item.key == key:
                del bucket[index]
                break
        else:
            raise KeyError(key)
        
    # create string representation
    # ambiguous, can look same as a dictionary with same contents
    def __str__(self) -> str:
        items = []
        for key, value in self.items:
            items.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(items) + "}"
    
    # create string representation
    # unambiguous, no other type of item will have same readout
    # but isn't necessarily unique - a copy would have same readout
    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"{cls}.from_dict({str(self)})"
    
    # can use equality (and inequality implicitly)
    # __ne__() does not equal (!=)
    def __eq__(self, comp):
        if self is comp:
            return True
        if type(self) is not type(comp):
            return False
        return set(self.items) == set(comp.items)
    
    def clear(self):
        for key in self.keys:
            del self[key]

    def update(self, *others, **kwothers):
        for other in others:
            if type(other) == set:
                raise TypeError("set cannot yield key-value pairs")
            elif type(other) == dict:
                for key, value in other.items():
                    self[key] = value
            elif len(other) != 2:
                raise ValueError("update method requires key-value pairs")
            else:
                self[other[0]] = other[1]

    
        for key, value in kwothers.items():
            self[key] = value
            
    def copy(self):
        return HashTable.from_dict(dict(self.items), self.capacity)
            
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
        
    # Used to get the hashed index of a key
    # Refactored from 3 other functions at this point
    def _index(self, key):
        return hash(key) % self.capacity
        
    def _resize_and_rehash(self):
        copy = HashTable(self.capacity * 2)
        for key, value in self.items:
            copy[key] = value
        self._buckets = copy._buckets
    
    # Generates a hash_table from a dictionary
    # Multiplies capacity by 10 to get more space for hashing
    @classmethod
    def from_dict(cls, dictionary: dict, capacity=None):
        hash_table = cls(capacity or len(dictionary) * 20)
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table
    
    # this decorator turns this method into a property
    # meaning it is not called like in a dict, but is accessed
    # i.e. HashTable.items, rather than HashTable.items()
    @property
    def items(self):
        return {
            item for bucket in self._buckets for item in bucket
            }

    @property
    def values(self):
        return [item.value for item in self.items]
    
    @property
    def keys(self):
        return {item.key for item in self.items}
    
    @property
    def capacity(self):
        return len(self._buckets)
    
    # Load factor is the ratio of filled slots to empty slots
    @property
    def load_factor(self):
        return len(self) / self.capacity
    
    # shows that size will increase when at load threshold
    def _show_capacity(self):
        for i in range(int(128 * self._load_factor_threshold)):
            num_pairs = len(self)
            num_empty = self.capacity - num_pairs
            print(
                f"{num_pairs:>2}/{self.capacity:>2}",
                ("X" * num_pairs) + ("." * num_empty)
            )
            self[i] = i

# as lft increases, space complexity decreases, but 
# time complexity in CRUD operations increases
test_hash = HashTable(load_factor_threshold=0.75)
test_hash._show_capacity()
