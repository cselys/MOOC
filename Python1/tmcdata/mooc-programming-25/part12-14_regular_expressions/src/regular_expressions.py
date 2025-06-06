# Write your solution here
import re

def is_dotw(my_string: str):
    expression = 'Mon|Tue|Wed|Thu|Fri|Sat|Sun'
    if re.search(expression, my_string):
        return True
    else:
        return False

def all_vowels(my_string: str):
    if re.search("^[aeiou]+$", my_string):
        return True
    else:
        return False 

def time_of_day(my_string: str):
    if re.search("^([0-1]\d|2[0-3]):[0-5][0-9]:[0-5][0-9]$", my_string):
        return True
    else:
        return False 

# def time_of_day(my_string: str):
#     return re.search("^([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", my_string) is not None
