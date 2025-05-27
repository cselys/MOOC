# Write your solution here
def invert(dictionary: dict):
    for key in list(dictionary.keys()):
        val = dictionary.pop(key)
        dictionary[val] = key
