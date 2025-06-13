#!/usr/bin/env python3

import sys
import math

def getdeviation(nums: []):
    avg = sum(nums)/len(nums)
    sums = 0
    for num in nums:
        sums += (num - avg) ** 2

    return math.sqrt(sums / (len(nums) - 1))

def summary(filename):
    with open(filename) as f:
        nums = []
        for line in f:
            try:
                nums.append(float(line))
            except ValueError:
                print("converstion error")

    return (round(sum(nums), 6),round(sum(nums)/len(nums), 6),round(getdeviation(nums), 6))

def main():
    for i in range(1, len(sys.argv)):
        t = summary(sys.argv[i])
        print(f"File: {sys.argv[i]} Sum: {t[0]:.6f} Average: {t[1]:.6f} Stddev: {t[2]:.6f}")

if __name__ == "__main__":
    main()
