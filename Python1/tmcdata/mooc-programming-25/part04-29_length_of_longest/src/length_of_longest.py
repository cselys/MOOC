# Write your solution here
def length_of_longest(my_list):
    longest = 0
    for astr in my_list:
        if len(astr) > longest:
            longest = len(astr)
    return longest