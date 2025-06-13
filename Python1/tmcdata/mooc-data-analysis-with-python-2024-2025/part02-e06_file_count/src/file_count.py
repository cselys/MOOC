#!/usr/bin/env python3

import sys

def file_count(filename):
    lines = 0
    words = 0
    characters = 0
    with open(filename) as f:
        for line in f:
            lines += 1
            for ch in line:
                characters += 1
            wordsinline = line.split()
            words += len(wordsinline)
                
    return (lines, words, characters)

def main():
    for i in range(1, len(sys.argv)):
        nums = file_count(sys.argv[i])
        print(f"{nums[0]}\t{nums[1]}\t{nums[2]}\t{sys.argv[i]}")

if __name__ == "__main__":
    main()
