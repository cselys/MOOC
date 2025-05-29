# Write your solution here
import urllib.request
import json

def retrieve_all():
    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
   # add a second argument to the function call
    request = urllib.request.urlopen(address)
    courses = json.loads(request.read())
    res_list = []
    for course in courses:
        if course["enabled"]:
            res = (course["fullName"], course["name"], course["year"], sum(course["exercises"]))
            res_list.append(res)  

    return res_list

def retrieve_course(course_name: str):
    address = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    request = urllib.request.urlopen(address)
    course = json.loads(request.read())
    res_dict = {}
    res_dict["weeks"] = len(course)
    students = []
    hours = []
    exercise = []
    for weeknum, week in course.items():
        students.append(week["students"])
        hours.append(int(week["hour_total"]))
        exercise.append(int(week["exercise_total"]))
        
    res_dict["students"] = max(students)
    res_dict["hours"] = sum(hours)
    res_dict["hours_average"] = res_dict["hours"]//res_dict["students"]
    res_dict["exercises"] = sum(exercise) 
    res_dict["exercises_average"] = res_dict["exercises"]//res_dict["students"]

    return res_dict

# retrieve_course("docker2019")