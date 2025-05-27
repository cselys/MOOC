# write your solution here
def largest():
    large = 0
    with open("numbers.txt") as new_file:
        for line in new_file:
            if int(line) > large:
                large = int(line)
    return large

# def largest():
#     with open("numbers.txt") as file:
#         start = True
#         biggest = 0
#         for number in file:
#             if start or int(number) > biggest:
#                 biggest = int(number)
#                 start = False
#         return biggest