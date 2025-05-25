# Write your solution here
def most_common_character(my_str):
    most = 0
    ch = ''
    for c in my_str:
        cnum = my_str.count(c)
        if cnum > most:
            most = cnum
            ch = c
    return ch