# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []
        self.heights = 0
        self.short = None

    def is_empty(self):
        return len(self.persons) == 0

    def add(self, person: Person):
        self.persons.append(person)
        self.heights += person.height
        if self.short is None or self.short.height > person.height:
            self.short = person

    def print_contents(self):
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {self.heights} cm")
        for p in self.persons:
            print(f"{p.name} ({p.height} cm)")

    def shortest(self): 
        if self.short is None:
            return None
        else:
            return self.short

    def remove_shortest(self):
        s = self.shortest()
        if s is not None:
            index = -1
            for p in self.persons:
                index += 1
                if p.name == s.name:
                    break
            if index >= 0:
                self.persons.pop(index)
        return s
