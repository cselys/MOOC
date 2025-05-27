# Write your solution here
def oldest_person(people: list):
    old = people[0]
    for person in people:
        if person[1] < old[1]:
            old = person
    return old[0]