# Write your solution here
def add_student(students:dict, name:str):
    students[name] = []

def print_student(students:dict, name:str):
    if name not in students:
        print(f"{name}: no such person in the database")
    else:
        print(f"{name}:")
        if not students[name]:
            print(" no completed courses")
        else:
            print(f" {len(students[name])} completed courses:")
            average_grade = 0
            for tu in students[name]:
                print(f"  {tu[0]} {tu[1]}")
                average_grade += tu[1]
            print(" average grade", average_grade/len(students[name]))

def add_course(students:dict, name:str, course:tuple):
    if name not in students:
        students[name] = []
    if course[1] > 0:
        found = ()
        for tu in students[name]:
            if tu[0] == course[0]:
                if tu[1] <= course[1]:
                    found = tu
                else:
                    found = course
        students[name].append(course)
        if found:
            students[name].remove(found) 
# def summary(students: dict):

#     students 2
# most courses completed 3 Peter
# best average grade 4.5 Eliza

# def main():
#     students = {}
#     add_student(students, "Peter")
#     add_course(students, "Peter", ("Introduction to Programming", 3))
#     add_course(students, "Peter", ("Advanced Course in Programming", 2))
#     add_course(students, "Peter", ("Data Structures and Algorithms", 0))
#     add_course(students, "Peter", ("Introduction to Programming", 2))
#     print_student(students, "Peter")

# main()
