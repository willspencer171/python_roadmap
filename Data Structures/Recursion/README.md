# Recursion
## What a bitch. I just can't wrap my head around you at the moment.
---
I love problems like this. I've always thought that recursion was a power- and time-intensive process that just eats up memory since it uses and abuses the call stack. I'm not entirely wrong, sometimes recursion can lead to HORRIBLE time complexities when compared with nice simple loops, but sometimes can lead to vast improvements.

Recursion, I hate you. I don't know that I'll ever fully understand you, but I'll let the world know when I do, on this README actually.

This set of tasks comes from [Geeks for Geeks](https://www.geeksforgeeks.org/recursion-practice-problems-solutions/) (surprise surprise) and it's really extensive. Some problems are just reframes of the same thing, but all in all, good practice. I'll just be continuing with these tasks every now and then when I feel I need humbling.

I'm learning a lot from these tasks. Here's what I know now that I didn't before:
>- Recursion uses the call stack. Since it's a stack, it's a LIFO structure and previous function calls are popped off one by one when returning.
>- When at the deepest points of recursion, sometimes you want to get data out immediately without traversing back up the recursion tree, which is difficult with just `return` statements.
>   - `yield` and `yield from` are my best friends now (I'm proud of Task 5). They allow me to get data from the top of the stack to the bottom of the stack without losing any information from other points at the bottom of the recursion tree so they can be stored and iterated through - _sexy_
>- All recursive functions can be reframed as a loop. Yes, ___all___ of them
>   - Conditions for ending recursion are if something returns truthy, that for loops is if something is false.
>   - `while True` - ends if false
>   - `if True ... return` ends if true
>- Interestingly, also found that any iterable can be unpacked using an asterisk *, including strings
>- Recursion can be good if you need to modify multiple parameters through each iteration (recursion) since they get passed into the next call

Reminder: `return` on its own returns nothing. Obviously. But it still gets you to the previous node on the recursion tree.
`yield` *temporarily* rescinds control back to the caller function, `return` ends the function and goes back to whatever the function before was doing.

As always, please feel free to provide **constructive** criticisms by reaching out to me on [Instagram](https://www.instagram.com/will_spencer171) or [LinkedIn](https://www.linkedin.com/in/willspencer171). I'm always learning and people always have opinions so let me hear them!

Thanks for reading!