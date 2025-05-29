# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
    result = []
    for i in range(amount):
        result.append(Fraction(1, amount))
    return result

# print(fractionate(3))

# fraction = Fraction(1, amount)
 
#     return [fraction] * amount