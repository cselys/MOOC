#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    # b = a[:,c]   # get column c
    # _,s,t = np.unique(b, return_inverse=True, return_counts=True)
    # idx = np.argsort(t[s])
    # return a[idx][::-1]

    d = {}
    for num in np.unique(a[:,c]):
        d[num] = []
    for i in np.argsort(a[:,c]):
        d[a[i,c]].append(i)
    sorted_dict = dict(sorted(d.items(), key=lambda item:len(item[1]), reverse=True))
    idxs = []
    for i in sorted_dict.values():
        idxs += i
    return a[idxs]

def main():
#     a = np.array(
#  [[5, 0, 3, 3, 7, 9, 3, 5, 2, 4],
#  [7, 6, 8, 8, 1, 6, 7, 7, 8, 1],
#  [5, 9, 8, 9, 4, 3, 0, 3, 5, 0],
#  [2, 3, 8, 1, 3, 3, 3, 7, 0, 1],
#  [9, 9, 0, 4, 7, 3, 2, 7, 2, 0],
#  [0, 4, 5, 5, 6, 8, 4, 1, 4, 9],
#  [8, 1, 1, 7, 9, 9, 3, 6, 7, 2],
#  [0, 3, 5, 9, 4, 4, 6, 4, 4, 3],
#  [4, 4, 8, 4, 3, 7, 5, 5, 0, 1],
#  [5, 9, 3, 0, 5, 0, 1, 2, 4, 2]])

    a = np.random.randint(0,10, (10, 10))
    most_frequent_first(a,-1)

if __name__ == "__main__":
    main()
