from insertion_sort import insertion_sort
from merge_sort import merge

def timsort(array):
    min_run = 32
    n = len(array)

    # Start by slicing and sorting small portions of the
    # input array. The size of these slices is defined by
    # your `min_run` size.
    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    # Now you can start merging the sorted slices.
    # Start from `min_run`, doubling the size on
    # each iteration until you surpass the length of
    # the array.
    size = min_run
    while size < n:
        # Determine the arrays that will
        # be merged together
        for start in range(0, n, size * 2):
            # Compute the `midpoint` (where the first array ends
            # and the second starts) and the `endpoint` (where
            # the second array ends)
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))

            # Merge the two subarrays.
            # The `left` array should go from `start` to
            # `midpoint + 1`, while the `right` array should
            # go from `midpoint + 1` to `end + 1`.
            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])

            # Finally, put the merged array back into
            # your array
            array[start:start + len(merged_array)] = merged_array

        # Each iteration should double the size of your arrays
        size *= 2

    return array

'''
This is a more complex sort that takes advantage of the fact that insertion sort is
speedy for small datasets (it insert sorts small subsets)
Then, it uses the merge function from merge_sort to merge sorted subsets together

This is an algorithm with O(n log n) average time complexity (better than O(n log n))
but the best case matches the merge sort's best case of O(n)

This leads to more consistently quick sorting over a large dataset without compromising
too much on space as per quick and merge sorts. It's just v good

The min_run value is used to determine the smallest length of an array to be
insert sorted before it is merged. This should best be a power of 2 so that equally
divided initial arrays can be re-merged nicely, but this isn't always possible
so there are ways to find the ideal min_run, so long as it's between 16 and 128, ideally
'''
