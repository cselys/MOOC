# Write your solution here
# You can test your function by calling it within the following block
   
if __name__ == "__main__":
    line(5, "x")


def line(num, character):
    if character != "":
        print(character[0]*num)
    else:
        print("*"*num)
 