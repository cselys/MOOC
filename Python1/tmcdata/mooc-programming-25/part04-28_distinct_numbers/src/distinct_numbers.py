# Write your solution here
def distinct_numbers(my_list):
    new_list = []
    for num in my_list:
        if num not in new_list:
            new_list.append(num)
    return sorted(new_list)