#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    a2 = a ** 2
    return np.sqrt(a2.sum(axis=1))
    # return np.sqrt(np.sum(a**2, axis=1))

def main():
    a=np.random.randn(5, 3)
    print(vector_lengths(a))

if __name__ == "__main__":
    main()
