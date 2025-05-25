# Write your solution here
def all_the_longest(my_str):
    longest = 0
    res = []
    for astr in my_str:
        if len(astr) > longest:
            longest = len(astr)

    for astr in my_str:
        if len(astr) == longest:
            res.append(astr)
    return res
 