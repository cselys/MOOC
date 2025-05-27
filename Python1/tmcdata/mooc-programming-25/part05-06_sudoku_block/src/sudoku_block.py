# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    numlist = []
    for r in range(3):
        for w in range(3):
            num = sudoku[row_no + r][column_no + w]
            if num > 0 and num in numlist:
                return False
            numlist.append(num)
    return True