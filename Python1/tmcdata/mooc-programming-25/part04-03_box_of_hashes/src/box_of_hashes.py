# Copy here code of line function from previous exercise
def line(num, character):
    if character != "":
        print(character[0]*num)
    else:
        print("*"*num)
 
def box_of_hashes(height):
    # You should call function line here with proper parameters
    while height > 0:
        line(10, "#")
        height -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)

