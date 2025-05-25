# Write your solution here
def no_shouting(my_list):
    result = []
    for astr in my_list:
        if astr.isupper():
            continue
        result.append(astr)
    return result