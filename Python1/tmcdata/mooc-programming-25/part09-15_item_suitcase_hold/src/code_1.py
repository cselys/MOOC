# Write your solution here:
class Item:
    def __init__(self, name: str, weight:int):
        self.__name = name
        self.__weight = weight
    
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
    def __init__(self, maxweight:int):
        self.__maxweight = maxweight
        self.__items = []
        self.__total = 0

    def add_item(self, item: Item):
        if self.__total + item.weight() <= self.__maxweight:
            self.__items.append(item)
            self.__total += item.weight()

    def __str__(self):
        num = len(self.__items)
        if num == 1:
            return f"{num} item ({self.__total} kg)"
        else:
            return f"{num} items ({self.__total} kg)"

    def weight(self):
        return self.__total

    def print_items(self):
        for i in self.__items:
            print(f"{i.name()} ({i.weight()} kg)")

    def heaviest_item(self):
        res = self.__items[0]
        for i in self.__items:
            if i.weight() > res.weight():
                res = i
        return res

if __name__ == "__main__":
    suitcase = Suitcase(25)
    item = Item("ABC Book", 2)
    suitcase.add_item(item)
    suitcase.weight()