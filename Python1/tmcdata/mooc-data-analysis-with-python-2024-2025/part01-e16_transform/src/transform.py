#!/usr/bin/env python3
import numpy as np

def transform(s1, s2):
    if not s1 or not s2:
        return []
    L = list(zip(map(int, s1.split(" ")), map(int, s2.split(" "))))
    return list(map(lambda x:x[0]*x[1], L))

def main():
    L1 = np.random.randint(-100, 100, 3)
    L2 = np.random.randint(-100, 100, 3)
    s1 = " ".join(map(str, L1))
    s2 = " ".join(map(str, L2))
    print(transform(s1, s2))

if __name__ == "__main__":
    main()

#   return [ a*b for (a, b) in zip(map(int, s1.split()), map(int, s2.split())) ]