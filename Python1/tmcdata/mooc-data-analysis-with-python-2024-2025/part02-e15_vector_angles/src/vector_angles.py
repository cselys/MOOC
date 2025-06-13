#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    # np.arccos(X*Y/np.abs(X))
    print(np.innder(X,Y))
    np.array([])

def main():
    A=np.array([[0,0,1], [-1,1,0]])
    B=np.array([[0,1,0], [1,1,0]])
    vector_angles(A,B)

if __name__ == "__main__":
    main()
