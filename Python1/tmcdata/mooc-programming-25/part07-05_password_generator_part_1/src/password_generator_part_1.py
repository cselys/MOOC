# Write your solution here
from string import ascii_lowercase
from random import randint

def generate_password(amount: int):
    res = []
    for i in range(amount):
        res.append(ascii_lowercase[randint(0,25)])
    return "".join(res)

# from random import choice
# from string import ascii_lowercase
 
# def generate_password(length: int):
#     passwd = ""
#     for i in range(length):
#         passwd += choice(ascii_lowercase)
 
#     return passwd