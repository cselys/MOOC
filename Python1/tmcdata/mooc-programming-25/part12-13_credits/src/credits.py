from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(attempts: list):
    return reduce(lambda res, attempt: res + attempt.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    return reduce(lambda res, attempt: res + attempt.credits, filter(lambda item: item.grade > 0, attempts), 0)

def average(attempts: list):
    grades = list(filter(lambda item: item.grade > 0, attempts))
    return  reduce(lambda res, attempt: res + attempt.grade, grades, 0)/len(grades)

if __name__=="__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Programming Course", 4, 5)
    s3 = CourseAttempt("Algorithms", 3, 0)
    print(average([s1, s2, s3]))