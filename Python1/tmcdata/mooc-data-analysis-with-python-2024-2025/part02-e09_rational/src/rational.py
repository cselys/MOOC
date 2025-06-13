#!/usr/bin/env python3

class Rational(object):
    def __init__(self, num1: int, num2: int):
        self.nums = [num1, num2]
        self.real = num1 / num2

    def __str__(self):
        return f"{self.nums} = {self.real}"

    def __mul__(self, another):
        return self.real * another.real

    def __add__(self, another):
        return (self.nums[0] * another.nums[1] + self.nums[1] * another.nums[0]) / (self.nums[1] * another.nums[1])

    def __sub__(self, another):
        return (self.nums[0] * another.nums[1] - self.nums[1] * another.nums[0]) / (self.nums[1] * another.nums[1])


    def __truediv__(self, another):
        return self.real / another.real
    
    def __eq__(self, another):
        return self.real == another.real
    
    def __gt__(self, another):
        return self.real > another.real
    
    def __lt__(self, another):
        return self.real < another.real

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
