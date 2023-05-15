from random import randint
from insertion_sort import insertion_sort

def _quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return _quicksort(low) + same + _quicksort(high)

def quicksort(array):
    # If array is small, use insertion sort as this
    # is quicker on small data despite higher complexity
    if len(array) < 128:
        return insertion_sort(array)

    return _quicksort(array)
'''
Time complexity for quicksort
This is a very similar approach to sorting to the merge sort

It uses the divide and conquer method to split the array at a random point
then put the smaller items to the left and the larger items to the right

Because this uses the 'same' variable, it splits the array fewer times,
which is lovely. This doesn't change the time complexity but does change
the speed with which the sort can be done

Time complexity for this is O(n log n) since it is a loop
dependent on recursion rather than a loop

Using a random pivot is high-risk high-reward:
worst case scenario is when the first or last index in an unsorted
list is picked, leading to a sublist of n-1 rather than n/2
On the other hand, setting the pivot to the median guarantees O(n)
complexity rather than O(log n) average-case. The randomness just
increases the chance that the optimal pivot is chosen since the median
isn't always optimal, depending on the initial order of items
'''
