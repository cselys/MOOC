#!/usr/bin/env python3

def interleave(*lists):
    res = []

    for x in list(zip(*lists)):
        res.extend(list(x))

    return list(res)

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
