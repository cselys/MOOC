# Write your solution here
def  count_matching_elements(my_matrix: list, element: int):
    count = 0
    for row in my_matrix:
        count += row.count(element)
    return count