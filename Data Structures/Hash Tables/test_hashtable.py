from hashtable import *
import pytest
from pytest_unordered import unordered
from unittest.mock import patch
from collections import deque

def test_hash_table():
    assert len(HashTable(capacity=3)) == 0

def test_hash_is_iterable():
    assert iter(HashTable(3)) is not None

def test_hash_yields_on_iterate():
    assert [item for item in HashTable(3)._slots] == [deque([]), deque([]), deque([])]

def test_should_create_empties():
    assert HashTable(3)._slots == [deque([]), deque([]), deque([])]

@pytest.mark.skip
def test_adding_doesnt_increase_size():
    test_hash = HashTable(100)
    test_hash["Hola"] = "hello"

def test_can_add_to_hash_table():
    test_hash = HashTable(100)
    value = "test_value"

    test_hash["Hola"] = "hello"
    test_hash[12] = "twelve"
    test_hash[value] = "It worked!"

    assert ("Hola", "hello") and (12, "twelve") and (value, "It worked!") in test_hash.items
    assert len(test_hash) == 3

def test_can_find_value_by_key():
    test_hash = HashTable(100)
    value = "test_value"

    test_hash["Hola"] = "hello"
    test_hash[12] = "twelve"
    test_hash[value] = "It worked!"

    assert test_hash["Hola"] == "hello" 
    assert test_hash[12] == "twelve" 
    assert test_hash[value] == "It worked!"

def test_unresolved_search_raises_error():
    test_hash = HashTable(100)
    
    with pytest.raises(KeyError) as exception_info:
        test_hash["missing key"]
    
    assert exception_info.value.args[0] == "missing key"


def test_should_find_value():
    test_hash = HashTable(100)
    test_hash["hola"] = "hola"
    assert "hola" in test_hash # also means test_hash.keys()

def test_should_not_find_missing_value():
    test_hash = HashTable(100)
    assert "missing_key" not in test_hash

def test_get_returns_sought_value():
    test_hash = HashTable(100)
    test_hash["hola"] = "hello"
    assert test_hash.get("hola", "default") == "hello"

def test_get_returns_default_value():
    test_hash = HashTable(100)
    test_hash["hola"] = "hello"
    assert test_hash.get("missing_key", "default") == "default"

def test_can_delete_item():
    test_hash = HashTable(100)
    test_hash["hola"] = "hello"
    assert ("hola", "hello") in test_hash.items
    assert len(test_hash) == 1

    del test_hash["hola"]

    assert ("hola", "hello") not in test_hash.items
    assert len(test_hash) == 0

def test_raises_error_when_del_missing_key():
    test_hash = HashTable(100)
    test_hash["hola"] = "hello"

    with pytest.raises(KeyError) as exception_info:
        del test_hash["missing_key"]

    assert exception_info.value.args[0] == "missing_key"

def test_can_update_value():
    test_hash = HashTable(100)
    test_hash["hola"] = "hello"
    assert test_hash["hola"] == "hello"

    test_hash["hola"] = "hallo"

    assert test_hash["hola"] == "hallo"
    assert len(test_hash) == 1

def test_hash_has_no_single_none_values():
    test_hash = HashTable(100)
    assert None not in test_hash.values

def test_should_return_copy_of_pairs():
    test_hash = HashTable(100)
    assert test_hash.items is not test_hash.items

def test_copy_of_pairs_has_no_none_PAIRS():
    test_hash = HashTable(100)
    assert None not in test_hash.items

def test_returns_value_list():
    test_hash = HashTable(100)
    test_hash["Spanish"] = "hola"
    test_hash["Alice"] = 24
    test_hash["Bob"] = 42
    test_hash["Joe"] = 42
    assert unordered(test_hash.values) == ["hola", 42, 24, 42]

@pytest.mark.skip
def test_keys_returned_as_set_no_duplicates():
    test_hash = HashTable(100)
    test_hash["Spanish"] = "hola"
    test_hash["Alice"] = 24
    test_hash["Bob"] = 42
    test_hash["Joe"] = 42

    assert type(test_hash.keys) == set

def test_returns_keys_set():
    test_hash = HashTable(100)
    test_hash["Spanish"] = "hola"
    test_hash["Alice"] = 24
    test_hash["Bob"] = 42
    test_hash["Joe"] = 42
    # unordered ignores the order that a list is presented in
    # this line basically says "check if all the items are there",
    # but doesn't need to compare like for like in terms of index
    assert unordered(test_hash.keys) == ["Joe", "Bob", "Alice", "Spanish"]

def test_pairs_are_a_set():
    test_hash = HashTable(100)
    test_hash["Spanish"] = "hola"
    test_hash["Alice"] = 24
    test_hash["Bob"] = 42
    test_hash["Joe"] = 42

    assert test_hash.items == [
    ("Spanish", "hola"),
    ("Alice", 24),
    ("Bob", 42),
    ("Joe", 42)
    ]

def test_pairs_of_list_type():
    test_hash = HashTable(100)
    assert test_hash.items == list()

def can_convert_to_dict():
    test_hash = HashTable(100)
    test_hash["Spanish"] = "hola"
    test_hash["Alice"] = 24
    test_hash["Bob"] = 42
    test_hash["Joe"] = 42

    dictionary = dict(test_hash)
    assert set(dictionary.keys()) == test_hash.keys
    assert set(dictionary.items()) == test_hash.items
    assert list(dictionary.values()) == unordered(test_hash.values)

def test_hash_must_have_positive_capacity():
    with pytest.raises(ValueError):
        HashTable(0)
        HashTable(-1)

def test_hash_table_size_must_be_integer():
    with pytest.raises(TypeError):
        HashTable("hello")

@pytest.mark.skip # Doesn't require explicit size setting
def test_size_must_have_value():
    with pytest.raises(TypeError) as error:
        HashTable()

def test_can_return_capacity():
    test_hash = HashTable(100)
    test_hash["Spanish"] = "hola"
    test_hash["Alice"] = 24
    test_hash["Bob"] = 42

    assert test_hash.capacity == 100

def test_has_string_rep():
    test_hash = HashTable(100)
    test_hash["Spanish"] = "hola"

    assert str(test_hash) == """{'Spanish': 'hola'}"""

def test_can_generate_from_dict():
    dictionary = {"Spanish": "hola", "English": "hello", "German": "hallo"}

    test_hash = HashTable.from_dict(dictionary)

    assert test_hash.capacity == len(dictionary) * 20
    assert test_hash.keys == list(dictionary.keys())
    assert test_hash.items == list(dictionary.items())
    assert unordered(test_hash.values) == list(dictionary.values())

def test_can_generate_from_dict_with_custom_capacity():
    dictionary = {"Spanish": "hola", "English": "hello", "German": "hallo"}

    test_hash = HashTable.from_dict(dictionary, 100)

    assert test_hash.capacity != len(dictionary) * 10
    assert test_hash.keys == list(dictionary.keys())
    assert test_hash.items == list(dictionary.items())
    assert unordered(test_hash.values) == list(dictionary.values())

def test_has_canonical_str_repr():
    test_hash = HashTable.from_dict({'hola': 'hello', 98.6: 37, False: True})

    assert repr(test_hash) in {
        "HashTable.from_dict({'hola': 'hello', 98.6: 37, False: True})",
        "HashTable.from_dict({'hola': 'hello', False: True, 98.6: 37})",
        "HashTable.from_dict({98.6: 37, 'hola': 'hello', False: True})",
        "HashTable.from_dict({98.6: 37, False: True, 'hola': 'hello'})",
        "HashTable.from_dict({False: True, 'hola': 'hello', 98.6: 37})",
        "HashTable.from_dict({False: True, 98.6: 37, 'hola': 'hello'})",
    }

test_hash = HashTable.from_dict({'hola': 'hello', 98.6: 37, False: True})

def test_hash_table_equal_to_itself():
    assert test_hash == test_hash

def test_hash_equal_to_copy():
    assert test_hash == test_hash.copy()        # Equal contents
    assert test_hash is not test_hash.copy()    # Not equal identity

def test_should_compare_equal_ignore_order():
    test_hash_2 = HashTable.from_dict({98.6: 37, 'hola': 'hello', False: True})
    
    assert test_hash == test_hash_2

def test_should_compare_unequality():
    test_hash_2 = HashTable.from_dict({"Completely": "Different"})
    
    assert test_hash != test_hash_2

def test_compare_unequal_with_diff_datatype():
    assert test_hash != 42

def test_copy_has_same_capacity_keys_values_and_pairs():
    copy = test_hash.copy()

    assert copy is not test_hash
    assert copy.capacity == test_hash.capacity
    assert set(copy.keys) == set(test_hash.keys)
    assert set(copy.items) == set(test_hash.items)
    assert copy.values == unordered(test_hash.values)

def test_compare_equal_not_identical():
    data = {"good morning": "america"}

    h1 = HashTable.from_dict(data, 100)
    h2 = HashTable.from_dict(data, 50)

    assert h1 == h2
    assert h1 is not h2

def test_can_clear_hash_table():
    assert test_hash == HashTable.from_dict({'hola': 'hello', 98.6: 37, False: True})
    test_hash.clear()

    assert len(test_hash) == 0
    assert len(test_hash.items) == 0
    assert len(test_hash._slots) == 60

def test_can_update_table():
    test_hash.update({3:2, "hi":"hello"}, [True, False], ("yes", "no"), foo="bar")
    assert (3, 2) in test_hash.items
    assert ("hi", "hello") in test_hash.items
    assert (True, False) in test_hash.items
    assert ('foo', "bar") in test_hash.items
    assert ("yes", "no") in test_hash.items

def test_raises_error_on_no_kv_pairs():
    with pytest.raises(ValueError) as e:
        test_hash.update(["hello", "hola", "bonjour"])
    
    assert e.value.args[0] == "update method requires key-value pairs"

# Patching is used to generate a mock value in the case of randomness
# @patch decorator
# OR
def test_should_detect_hash_collisions():
    assert hash("foobar") not in [1, 2, 3]
    # return_value takes one value,
    # side_effect takes a list of values
    with patch("builtins.hash", return_value=1):
        assert hash("foobar") == 1
    
    with patch("builtins.hash", side_effect=[1,2,3]):
        assert hash("foobar") == 1
        assert hash("foobar") == 2
        assert hash("foobar") == 3

# Linear probing follows, no TDD to come
# But I will still write tests
def test_():
    pass
