#!/usr/bin/env python3

def distinct_characters(L):
    res = {}
    for item in L:
        res[item] = len(set(item))
    return res

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
