# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if len(self.numbers) == 0:
            return 0
        return self.get_sum()/self.count_numbers()
     
def main():
    stats = NumberStats()
    while True:
        num = int(input("Please type in integer numbers:"))
        if num == -1:
            print(f"Sum of numbers: {stats.get_sum()}")
            print(f"Mean of numbers: {stats.average()}")
            break
        else:
            stats.add_number(num)
# main()