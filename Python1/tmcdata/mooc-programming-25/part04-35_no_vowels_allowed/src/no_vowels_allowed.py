# Write your solution here
def no_vowels(my_str):
    for ch in 'aeiou':
        my_str = my_str.replace(ch, '')
    return my_str