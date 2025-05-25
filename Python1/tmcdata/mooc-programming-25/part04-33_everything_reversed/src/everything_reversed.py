# Write your solution here
def everything_reversed(str_list):
    my_list = []
    for astr in str_list[::-1]:
        my_list.append(astr[::-1])
    return my_list