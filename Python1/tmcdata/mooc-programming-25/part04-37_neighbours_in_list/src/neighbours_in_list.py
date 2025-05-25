# Write your solution here
def longest_series_of_neighbours(my_list: list):
    longest = 0
    count = 1
    index = 0
    while index < len(my_list) - 1:
        if my_list[index] == my_list[index+1] + 1 or my_list[index] == my_list[index+1] - 1:
            count += 1
        else:
            if count > longest:
                longest = count
            count = 1
        index += 1
    if count > longest:
        return count
    return longest

    # def longest_series_of_neighbours(my_list: list):
    # longest = 1
    # result = 1
    # for i in range(1, len(my_list)):
    #     # function abs calculates the absolute value
    #     if abs(my_list[i-1]-my_list[i]) == 1:
    #         result += 1
    #     else:
    #         result = 1
    #     # function max returns the highest of the parameters
    #     longest = max(longest, result)
    # return longest