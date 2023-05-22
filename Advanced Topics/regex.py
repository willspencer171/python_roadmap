'''
Regex is a painfully powerful pattern matching system that can condense
complex patterns into a single string of characters
Only problem is, it's got disgusting notation

There are a thousand and one regex cheat sheets out there and they'll
all say the same thing. However, I highly recommend using ChatGPT to
write regex skeletons for you so you can adjust and fine-tune it

Otherwise, here's a run-down of what is going on in regex
'''
# https://regexone.com/ seems to be a good place to get some regex practice in

import re
'''re.compile(pattern, flags=0)
re.findall(string[, pos[, endpos]])
re.search(string[, pos[, endpos]])
re.match(string[, pos[, endpos]])
re.split(string, maxsplit=0)
re.sub(repl, string, count=0)'''

# These are the important methods of regex
# after saving compile to a variable, you can do the other methods
# from that variable e.g

pattern = re.compile(r"^\s*(.*)\s*$")
comma = re.compile(",\D")

# returns the matched string that follows the above pattern, `pattern`
m = pattern.match("     the quick brown fox     ")
print(m.group(0), m.group(1), sep=" <-- full length, cap group 1 --> ")

# splits the string according to the pattern above
# using the capturing group () retains the split sentinel in the result
str_split = comma.split("50,000 longboats, that's a lot of boats, I think!")
print(str_split)

# Regex is nice once you get the hang of it and it does just take practice
# but it is common sense at the end of the day

# This is my go-to cheatsheet: 
# https://cheatography.com/davechild/cheat-sheets/regular-expressions/
