# Write your solution here
# You can test your function by calling it within the following block
def spruce(num):
    longest = num * 2 - 1
    linenum = 1
    print("a spruce!")
    while linenum <= num:
        line = ""
        space = (longest - linenum * 2 + 1)//2 
        line += " " * space
        line += "*" * (linenum * 2 - 1)
        print(line)
        linenum += 1
    print(" " * ((longest - 1) //2) + "*")

if __name__ == "__main__":
    spruce(5)