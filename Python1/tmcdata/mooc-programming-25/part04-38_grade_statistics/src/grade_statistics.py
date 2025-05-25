# Write your solution here
def input_from_user():
    user_points = []
    while True:
        twonums = input("Exam points and exercises completed: ")
        if twonums == "":
            return user_points
        user_points.append(int(twonums.split()[0])) 
        user_points.append(int(twonums.split()[1]))   

def print_result(my_list):
    print("Statistics:")
    print(f"Points average: {my_list[0]:.1f}")
    print(f"Pass percentage: {my_list[1] * 100:.1f}")
    print("Grade distribution:")
    index = 5
    for star in my_list[2:]:
        print(f"  {index}:", "*" * star)
        index -= 1

def getgrade(my_list):
    grades = []
    for index in range(0, len(my_list)//2):
        grades.append(my_list[index*2] + my_list[index*2+1]//10)
    return grades

def analyze(my_list_double):
    my_list = getgrade(my_list_double)
    grades = []
    for point in my_list:
        if point < 15:
            grade = 0
        elif point < 18:
            grade = 1
        elif point < 21:
            grade = 2
        elif point < 24:
            grade = 3
        elif point < 28:
            grade = 4
        else:
            grade = 5
        grades.append(grade)
        
    index = 0
    while index < len(grades):
        if my_list_double[index*2] < 10:
            grades[index] = 0
        index += 1

    new_list = []
    new_list.append(sum(my_list) / len(my_list))
    new_list.append(1 - grades.count(0)/len(grades))  
    for i in range(5, -1, -1):
        new_list.append(grades.count(i))
    return new_list

def main():
    inputs = input_from_user()
    analysis_result = analyze(inputs)
    print_result(analysis_result)
    

main()