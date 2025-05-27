# Write your solution here
def longest(strings: list):
    longest = 0
    result = ""
    for string in strings:
        if len(string) > longest:
            longest = len(string)
            result = string
    return result