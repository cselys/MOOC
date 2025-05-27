# write your solution here
def line_list(line:str):
    nums = []
    for num in line.replace("\n","").split(","):
        nums.append(int(num))
    return nums

def matrix_sum():
    with open("matrix.txt") as new_file:
        total = 0
        for line in new_file:
            total += sum(line_list(line))
        return total

def matrix_max():
    with open("matrix.txt") as new_file:
        res = 0
        for line in new_file:
            res = max(res, max(line_list(line)))
        return res

def row_sums():
     with open("matrix.txt") as new_file:
        rowsums = []
        for line in new_file:
            rowsums.append(sum(line_list(line)))
        return rowsums

        