# Write your solution here
def row_correct(sodoku: list, row_no: int):
    for n in range(1,10):
        if sodoku[row_no].count(n) > 1:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    colcount = [0] * 10
    for row in sudoku:
        colcount[row[column_no]] += 1

    for n in colcount[1:]:
        if n > 1:
            return False
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    numlist = []
    for r in range(3):
        for w in range(3):
            num = sudoku[row_no + r][column_no + w]
            if num > 0 and num in numlist:
                return False
            numlist.append(num)
    return True

def sudoku_grid_correct(sudoku: list):
    for n in range(9):
        if row_correct(sudoku, n) is False or column_correct(sudoku, n) is False:
            return False
        if n % 3 == 0:
            if block_correct(sudoku, n, n) is False:
                return False
    return True
    