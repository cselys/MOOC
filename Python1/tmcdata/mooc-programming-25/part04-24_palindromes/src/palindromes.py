# Write your solution here
def palindromes(my_str):
    i = 0
    while i < len(my_str)//2:
        if my_str[i] != my_str[len(my_str) - 1 - i]:
            return False
        i += 1
    return True


# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def my_main():
    while True:
        astr = input("Please type in a palindrome: ")
        if palindromes(astr):
            print(astr, "is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")
my_main()
