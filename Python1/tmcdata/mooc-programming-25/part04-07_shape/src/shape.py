# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(num, character):
    if character != "":
        print(character[0]*num)
    else:
        print("*"*num)

def triangle(size, ch):
    # You should call function line here with proper parameters
    index = 0
    while index < size:
        index += 1
        line(index, ch)    

def square(wid, heigth, character):
    # You should call function line here with proper parameters
    index = 0
    while index < heigth:
        line(wid, character)
        index += 1

def shape(num1, ch1, num2, ch2):
    triangle(num1, ch1)
    square(num1, num2, ch2)

if __name__ == "__main__":
    shape(5, "X", 3, "*")