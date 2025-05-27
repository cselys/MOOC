# Write your solution here
def print_sudoku(sudoku: list):
    rindex = 0
    for row in sudoku:
        cindex = 0        
        for ch in row:
            if ch == 0:
                print("_", end=' ')
            else:
                print(f"{ch}", end=' ')

            cindex += 1  
            if cindex % 3 == 0:
                 print(" ", end='')
     
        print("", end ='\n')    
        rindex += 1
        if rindex % 3 == 0:
            print()

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number
            
