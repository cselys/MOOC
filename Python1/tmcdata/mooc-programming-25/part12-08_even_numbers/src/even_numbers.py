# Write your solution here
def even_numbers(start: int, end: int):
    num = start
    if num % 2 == 1:
        num += 1
    while num <= end:
        yield num
        num += 2