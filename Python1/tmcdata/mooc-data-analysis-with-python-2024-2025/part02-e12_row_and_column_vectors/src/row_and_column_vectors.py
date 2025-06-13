#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    return np.split(a, a.shape[0], axis=0)
    # res = []
    # parts = np.split(a, range(a.ndim), 1)
    # for row in a:
    #     res.append(row.reshape(1,a.shape[1]))
    # return res

def get_column_vectors(a):
    return np.split(a, a.shape[1], axis=1)
    # res = []
    # parts = np.split(a, range(a.ndim), 1)
    # for row in a.T:
    #     res.append(row.reshape(a.shape[0],1))
    # return res

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
