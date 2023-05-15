def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array

'''
Time complexity analysis of Bubble sort:
In a worst-case scenario (items are all in the wrong index), this
algorithm must pass over each element in the list twice.
Since there is a for loop inside a for loop, these passings are dependent
on each other and can be multiplied together.

Because each passing is linearly dependent on the size of the
list, the time complexity is O(n) * O(n) = O(n^2)

The best case is O(n) (if already sorted) where the inner for loop's
condition is never met.
'''
