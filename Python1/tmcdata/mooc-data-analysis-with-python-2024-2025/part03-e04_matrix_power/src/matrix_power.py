#!/usr/bin/env python3
import numpy as np
from functools import reduce

def matrix_power(a, n):
    if n == 0:
        return np.eye(a.shape[0])

    if n == 1:
        return a

    if n < 0:
        a_inv = list(np.linalg.inv(np.array(a)))
        return reduce(np.matmul, (a_inv for _ in range(-n)))

    return reduce(np.matmul, (a for _ in range(n)))  

def main():
    a = np.array([[1,2], [3,4]])
    matrix_power(a, 1)
    return

if __name__ == "__main__":
    main()



# def matrix_power(a, n):
#     if n >= 0:
#         return reduce(np.matmul, (a for _ in range(n) ), np.eye(a.shape[0]))
#     else:
#         inv = np.linalg.inv(a)
#         return reduce(np.matmul, (inv for _ in range(-n) ))