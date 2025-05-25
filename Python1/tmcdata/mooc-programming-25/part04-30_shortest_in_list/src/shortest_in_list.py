# Write your solution here
def shortest(my_list):
    res = my_list[0]
    shortest = len(res)
    for astr in my_list:
        if len(astr) < shortest:
            shortest = len(astr)
            res = astr
    return res
