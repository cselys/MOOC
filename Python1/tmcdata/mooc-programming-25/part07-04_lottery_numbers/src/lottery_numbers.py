# Write your solution here
from random import randint

def lottery_numbers(amount: int, lower: int, upper: int):
    res = []
    for i in range(amount):
        rint = randint(lower, upper)
        while rint in res:
            rint = randint(lower, upper)
        res.append(rint)
    
    return sorted(res)

