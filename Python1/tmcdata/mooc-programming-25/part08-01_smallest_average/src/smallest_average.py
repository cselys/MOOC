# Write your solution here
def average(person: dict):
    ex_sum = person["result1"]+person["result2"]+person["result3"]
    return ex_sum/3

def smallest_average(person1: dict, person2: dict, person3: dict):

    sum1 = average(person1)
    sum2 = average(person2)
    sum3 = average(person3)
    if sum1 < sum2 and sum1 < sum3:
        return person1
    else:
        if sum1 > sum2:
            return person2
        else:
            return person3