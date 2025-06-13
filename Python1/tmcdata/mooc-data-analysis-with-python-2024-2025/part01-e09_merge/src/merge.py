#!/usr/bin/env python3

def merge(L1, L2):
    i1, i2 = 0, 0
    res = []
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] < L2[i2]:
            res.append(L1[i1])
            i1 += 1
        else:
            res.append(L2[i2])
            i2 += 1
    if i2 < L1[i2] :
        res.extend(L2[i2:])
    if i1 < L1[i1]:
        res.extend(L1[i1:])
    return res

def main():
    L1 = [1, 5, 9, 12]
    L2 = [2, 6, 10]
    print(merge(L1, L2))

if __name__ == "__main__":
    main()
