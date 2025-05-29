# Write your solution here
import string

def separate_characters(my_string: str):
    part1 = []
    part2 = []
    part3 = []
    for ch in my_string:
        if ch in string.ascii_letters:
            part1.append(ch)
        elif ch in string.punctuation:
            part2.append(ch)
        else:
            part3.append(ch)
            
    return ("".join(part1), "".join(part2), "".join(part3))