def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array - 1)

    # Loop from the second element of the array until
    # the last element
    for i in range(left + 1, right + 1):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= left and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item

    return array

'''
Time complexity for Insertion sort:
Similar to the bubble sort, the insertion sort has a worst-case
complexity of O(n^2), because it has a loop within a loop, both of which will
pass over the whole list if perfectly unsorted

However, the runtime of the insertion sort is typically quicker because it
doesn't ~have~ to make a swap, whereas if a bubble sort doesn't make a swap,
it's only because the list is sorted.
All an insertion sort not making a change means is that it is already
in the right place, rather than saying that everything is

A bubble sort also only makes moves one index at a time, whereas the
insertion sort can move an element multiple places to get it in the right place

This makes insertion sort a very efficient algorithm for small datasets,
but the time complexity means that when the dataset size increases, it really slows down

Other algorithms have faster time complexities but are more resource intensive
'''
