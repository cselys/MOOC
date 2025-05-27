# Write your solution here
def transpose(matrix: list):
    for i in range(len(matrix)):
        j = i
        while j < len(matrix):
            swap = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = swap
            j = j + 1
