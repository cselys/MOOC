#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("iris.csv").drop('species', axis=1).values

def lengths():
    arr = load()
    (a,b) = scipy.stats.pearsonr(arr[:,0], arr[:,2])
    return a

def correlations():
    arr = load()
    return np.corrcoef(arr, rowvar=False)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
