# Write your solution here
def column_correct(sudoku: list, column_no: int):
    colcount = [0] * 10
    for row in sudoku:
        colcount[row[column_no]] += 1

    for n in colcount[1:]:
        if n > 1:
            return False
    return True