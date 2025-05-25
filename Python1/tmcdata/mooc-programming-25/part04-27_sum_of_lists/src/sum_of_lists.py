# Write your solution here
def list_sum(list1, list2):
    new_list = []
    for index in range(0, len(list2)):
        new_list.append(list1[index] + list2[index])
    return new_list