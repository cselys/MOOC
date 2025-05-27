# Write your solution here
def older_people(people: list, year: int):
    result = []
    for p in people:
        if p[1] < year:
            result.append(p[0])
    return result