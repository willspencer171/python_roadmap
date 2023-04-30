#! python3
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

class Pair(NamedTuple):
    key: Any
    value: Any

DELETED = object()

class HashTable:
    # Initialise class instance
    # load factor threshold is optional, means "at what percentage
    # would you like to resize the table?"
    def __init__(self, capacity=8, load_factor_threshold=0.6, separate_chaining=True):
        if type(capacity) != int:
            raise TypeError("Hash Table size must be an integer")
        if capacity < 1:
            raise ValueError("Capacity of hash table must be positive")
        self._separate_chaining = separate_chaining

        match self._separate_chaining:
            case True:
                from collections import deque
                self._slots = [deque() for _ in range(capacity)]
                self._probe = None
            case False:
                self._slots = [None] * capacity
                
        self._load_factor_threshold = load_factor_threshold
        # used to retain the insertion order of items
        # Now, items, keys and values can be output as lists
        # and keys and values can zip to generate a list of items
        self._keys = []
    
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

        match self._separate_chaining:
            case True:
                bucket = self._slots[self._index(key)]
                for index, item in enumerate(bucket):
                    if item.key == key:
                        bucket[index] = Pair(key, value)
                        break
                else:
                    bucket.append(Pair(key, value))
                    self._keys.append(key)
            
            case False:
                for index, item in self._probe(key):
                    if item is DELETED: continue
                    if item is None or item.key == key:
                        self._slots[index] = Pair(key, value)
                        self._keys.append(key)
                        break
    
    # retrieve item if exists
    # can use square bracket notation
    def __getitem__(self, key):
        match self._separate_chaining:
            case True:
                bucket = self._slots[self._index(key)]
                for item in bucket:
                    if item.key == key:
                        return item.value
                raise KeyError(key)
            
            case False:
                for _, item in self._probe(key):
                    if item is None:
                        raise KeyError(key)
                    if item is DELETED:
                        continue
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
        match self._separate_chaining:
            case True:
                bucket = self._slots[self._index(key)]
                for index, item in enumerate(bucket):
                    if item.key == key:
                        del bucket[index]
                        self._keys.remove(key)
                        break
                else:
                    raise KeyError(key)
            case False:
                for index, item in self._probe(key):
                    if item is None:
                        raise KeyError(key)
                    if item is DELETED:
                        continue
                    if item.key == key:
                        self._slots[index] = DELETED
                        self._keys.remove(key)
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
    
    # this is a refactored function for the CRUD functions,
    # Create, Read, Update, Destroy
    # Implements linear probing hash collision resolution
    def _probe(self, key):
        index = self._index(key)
        for _ in range(self.capacity):
            yield index, self._slots[index]
            index = (index + 1) % self.capacity
    
    def _resize_and_rehash(self):
        match self._separate_chaining:
            case True:
                copy = HashTable(self.capacity * 2)
                for key, value in self.items:
                    copy[key] = value
                self._slots = copy._slots

            case False:
                copy = HashTable(self.capacity * 2, separate_chaining=False)
                for key, value in self.items:
                    copy[key] = value
                self._slots = copy._slots
    
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
        match self._separate_chaining:
            case True:
                return [(key, self[key]) for key in self.keys]
            
            case False:
                return {
                    pair for pair in self._slots 
                    if pair not in (None, DELETED)
                    }

    @property
    def values(self):
        return [self[key] for key in self.keys]
    
    @property
    def keys(self):
        return self._keys.copy()
    
    @property
    def capacity(self):
        return len(self._slots)
    
    # Load factor is the ratio of filled slots 
    # (including deleted), to empty slots
    @property
    def load_factor(self):
        match self._separate_chaining:
            case True:
                return len(self) /  self.capacity
            case False:
                filled = [slot for slot in self._slots if slot]
                return len(filled) / self.capacity
    
    # shows that size will increase when at load threshold
    def _show_capacity(self, reps=78):
        for i in range(reps):
            num_pairs = len(self)
            num_empty = self.capacity - num_pairs
            print(
                f"{num_pairs:>2}/{self.capacity:>2}",
                ("X" * num_pairs) + ("." * num_empty)
            )
            self[i] = i

# as lft increases, space complexity decreases, but 
# time complexity in CRUD operations increases
test_hash_lin = HashTable(load_factor_threshold=0.6, separate_chaining=False)
test_hash_sep_chain = HashTable(load_factor_threshold=0.6)

print("Linear Probing")
test_hash_lin._show_capacity(15)
print("Separate Chaining")
test_hash_sep_chain._show_capacity(15)
