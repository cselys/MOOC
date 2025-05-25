# Write your solution here
def same_chars(mystr, num1, num2):
    strlen = len(mystr)
    if num1 >= strlen or num2 >= strlen:
        return False

    return mystr[num1] == mystr[num2]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))