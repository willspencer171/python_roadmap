#! python3
""" 
Task 1: Given a string, find all possible palindromic partitions of given string.
Example:    Input: nitin
            Output: n i t i n
                    n iti n
                    nitin
return if every substring is palindromic
"""
from string import ascii_letters, ascii_lowercase, digits
result = set()  # initialise as a set to prevent duplicates
def palin_part(input_str):
    # convert to list (it kind of is already but this means we can convert to tuple easier)
    input_str = [char.lower() for char in input_str if all(letter in ascii_letters for letter in char)] # reduce to lowercase letters, ignore case and punct
    
    # if the input is a single character, return that character
    if len(input_str) <= 1:
        return input_str[0]
    
    result.add(tuple(input_str))
    
    # range starts at 1 so it looks back AND forward (needs to check behind)
    for i in range(1, len(input_str)):
        # this only really happens after the first recursion
        # if the item before is equal to the current item's palindrome,
        # add it in
        # This groups together pairs, basically
        if input_str[i-1] == input_str[i][::-1]:
            palin_part(input_str[:i-1] + [input_str[i-1]+input_str[i]] + input_str[i+1:])
        
        # this groups pairs that have one group between them
        # That's all we're doing, grouping pairs
        if i+1 < len(input_str) and input_str[i-1] == input_str[i+1][::-1]:
            palin_part(input_str[:i-1] + [input_str[i-1]+input_str[i]+input_str[i+1]] + input_str[i+2:])

    return sorted(list(result))


print(palin_part("Do geese see God"))
print("Items:", len(palin_part("Do geese see God")))

"""
Task 2: Check if a number is Palindrome
This sounds really straightforward but if you want to use recursion, it isn't quite so
This takes advantage of the fact that the all-but-last digit of a base 10 number is num // 10
and the last one is num % 10
Recurse through num // 10 until you get to the first single digit, then build back up
"""

def single_digit(num):
    return (num >= 0 and
            num < 10)

def is_palindrome_util(num, copy_num):
    # copy_num is a shallow copy of num determined prior to this function call
    # this allows the same number to be manipulated in two ways without affecting the copy

    # Base case: required for recursion to end
    if single_digit(num):
        # Modulo is going to be used here
        # copy_num is technically a list containing just the number, hence [0]
        return num == copy_num[0] % 10
        # if this returns False, this triggers a cascade upwards,
        # stating that the number is not a palindrome
    
    # This is the important bit
    if not is_palindrome_util(num // 10, copy_num):
        # This never happens if something a palindrome
        return False                #   <---------------------------------------¬
    #                                                                           |
    # take off last digit                                                       |
    copy_num[0] = copy_num[0] // 10 #                                           |
    #                                                                           |
    # compare the last digits                                                   |
    # at this point, the nth digit of num is the -nth digit of the copy         |
    # if the last digits do not match, return false, and cascade upwards with falses
    return num % 10 == copy_num[0] % 10

# Driver / formatter - protects the number
def is_pal(num):
    if num < 0:
        num = -num
    
    return is_palindrome_util(num, [num])
print(is_pal(123561))

"""
Task 3: Print all possible strings of length k that can be formed from a set of n characters
SET IS NOT SUBSCRIPTABLE SO CONVERT TO SET THEN LIST TO REMOVE DUPES
"""
def all_strings(chars, length, update_set = set()):
    chars = list(set(chars))
    def _rec(set, prefix, k):
        # base case k=0
        """ Remember: base case is usually the end of a counter
        It's difficult to make one up since you have to know
        the end result but if you use a counter and decrement,
        that's usually a good place to start """
        if k == 0:
            update_set.add(prefix)
            return
        

        for i in range(len(set)):
            _prefix = prefix + set[i]
            _rec(set, _prefix, k - 1)
        
    _rec(chars, "", length)
    return update_set.copy()
    # Convenient side effect alongside output as parameter,
    # you can assign at the same time as update an existing set

output_ = set()
other_output = all_strings({*ascii_lowercase[:6]}, 6, output_)
zipped = zip(sorted(list(other_output)), sorted(list(output_)))
print("\nAre these two sets identical?", other_output is output_, sep="\n")

palins =[]
for item in output_:
    if item == item[::-1]:
        palins.append(item)

print(sorted(palins))

"""
Task 4: Write your own atoi()
This is weird, atoi basically converts a string representation of a number to an int
Our base case is gonna be a string of one character
We want to add the next number onto the end, basically tacking it on like if it were a string

Slowly getting the hang of this I think?
"""

def rec_atoi(string: str, num=0):
    # We want the string to only have numbers
    if not any(char in string for char in digits):
        return 0
    
    if len(string) == 0:
        return 0
    
    # base case, string is one char
    if len(string) == 1:
        return int(string) + 10 * num
    
    num = int(string[0:1]) + 10 * num
    
    return rec_atoi(string[1:], num)

print(rec_atoi("1235615312315648945646513"))
