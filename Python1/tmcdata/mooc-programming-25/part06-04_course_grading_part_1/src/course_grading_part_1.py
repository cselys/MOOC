# write your solution here

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

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

for id, name in student.items():
    print(f"{name} {exercises[id]}")