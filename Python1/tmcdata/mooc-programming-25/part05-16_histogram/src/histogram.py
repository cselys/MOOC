# Write your solution here
def histogram(my_str):
    d = {}
    for ch in my_str:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    
    for key in d:
        print(key, "*" * d[key])
