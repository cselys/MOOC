# write your solution here
def get_grade(num: int):
    if num < 15:
        return 0
    elif num < 18:
        return 1
    elif num < 21:
        return 2
    elif num < 24:
        return 3
    elif num < 28:
        return 4
    else:
        return 5

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exercises2.csv"

student = {}
i = 0
with open(student_info) as new_file:
    for line in new_file:
        if i == 0:
            i = i + 1
            continue
        else:
            line = line.replace("\n","")
            parts = line.split(";")
            student[parts[0]] = parts[1] + " " + parts[2]
        
exercises = {}
i = 0
with open(exercise_data) as new_file:
    for line in new_file:
        grades = []
        if i == 0:
            i = i + 1
            continue
        else:
            line = line.replace("\n","")
            parts = line.split(";")
            for grade in parts[1:]:
                grades.append(int(grade))
            exercises[parts[0]] = sum(grades)

exams = {}
with open(exam_data) as new_file:
    for line in new_file:
        parts = line.replace("\n", '').split(";")
        points = 0
        if parts[0] == 'id':
            continue
        else:
            for grade in parts[1:]:
                points += int(grade.strip())
            exams[parts[0]] = points + exercises[parts[0]]//4

for id, name in student.items():
    print(f"{name} {get_grade(exams[id])}")