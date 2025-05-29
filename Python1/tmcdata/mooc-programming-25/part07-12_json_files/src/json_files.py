# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()
        
    content = json.loads(data)

    for dicts in content:
        hob = []
        for h in dicts["hobbies"]:
            hob.append(h)   
        print(f"{dicts["name"]} {dicts["age"]} years ({", ".join(hob)})")

# print_persons("file1.json")

    # for person in persons:
    #     name = person['name']
    #     age = person['age']
    #     hobbies = ", ".join(person['hobbies'])
    #     print(f"{name} {age} years ({hobbies})")