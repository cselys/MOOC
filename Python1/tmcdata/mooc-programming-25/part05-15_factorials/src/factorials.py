# Write your solution here
def factorials(n: int):
    d = {}
    for i in range(1,n + 1):
        if i == 1:
            d[i] = i
        else:
            d[i] = d[i-1] * i
    return d
