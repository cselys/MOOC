# Write your solution here
import string

def change_case(orig_string: str):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    res = ""
    for ch in orig_string:
        if ch in lower:
            res += ch.upper()
        elif ch in upper:
            res += ch.lower()
        else:
            res += ch
    return res

def split_in_half(orig_string: str):
    half = len(orig_string) // 2
    return (orig_string[:half], orig_string[half:])

def remove_special_characters(orig_string: str):
    res = ""
    for ch in orig_string:
        if ch == " " or ch in string.digits or ch in string.ascii_letters:
            res += ch
    return res

if __name__ == "__main__":
    # testing functionality
    print(change_case("This is a test"))
    print(split_in_half("Here we are still testing"))
    print(remove_special_characters("One two three four five"))