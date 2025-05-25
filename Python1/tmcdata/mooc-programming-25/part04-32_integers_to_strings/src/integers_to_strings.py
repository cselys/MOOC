# Write your solution here
def formatted(my_str):
    res = []
    for num in my_str:
        res.append(f'{num:.2f}')
    return res