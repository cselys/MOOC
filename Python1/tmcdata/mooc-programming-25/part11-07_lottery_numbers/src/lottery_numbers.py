# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, num: int, nums: list):
        self.num = num
        self.nums = nums

    def number_of_hits(self, numbers: list):
        return len([n for n in numbers if n in self.nums])

    def hits_in_place(self, numbers):
        return [n if n in self.nums else -1 for n in numbers]