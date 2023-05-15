# Sorting Algorithms

## A quick overview of sorting algorithms and a dip into their time complexities

I remember doing a small section of my Computing A level about sorting algorithms - yet another thing I can hear in good ol' Rob's voice! Sorting algorithms do what they say on the tin. Some are faster and others are not so fast. Each has a tradeoff and there isn't a perfect sorting algorithm (unless you're a real fan of Timsorts which I have become)

I have a selection of common sorting algorithms used in Python, as well as a simple explanation of their big O time-complexity expression. Big O notation for time complexity makes sense to me, much more so than that for space complexity - it's a measure of how the time an algorithm is expected to take scales with the size of input data. I assume the same is true for space complexity but with regards to how much *memory* is being used. I don't imagine it's about how much storage is used if there are no I/O operations

>### What have I learned?
>
>- In short, a little bit about a few things.
>- Big O notation
>   - Time complexity is a measure of how we expect the amount of processing time to increase with respect to the size of the data being passed to an algorithm. There is a hierarchy of expressions, the fastest of which being O(1) (constant)
>   - I kind of liken this to the reaction order that I saw so much of in my kinetics modules at uni. However, the reaction order can only be with respect to the slowest (worst-case) part of a reaction, otherwise, every reaction has no limit on best-case scenario i.e every best case scenario is O(1)
>- Different sorting algorithms!
>   - Bubble and insertion sorts are done using nested loops, giving them a time complexity of O(n<sup>2</sup>)
>   - Merge and quicksort use a loop and recursion instead, giving them a time complexity of O(n log n). This is offset by the increase in space complexity due to the use of the call stack data structure

As always, please feel free to provide **constructive** criticisms by reaching out to me on [Instagram](https://www.instagram.com/will_spencer171) or [LinkedIn](https://www.linkedin.com/in/willspencer171). I'm always learning and people always have opinions so let me hear them!
