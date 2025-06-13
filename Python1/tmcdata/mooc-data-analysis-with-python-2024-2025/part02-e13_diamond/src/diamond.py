#!/usr/bin/env python3

import numpy as np

def diamond(n):
    base = np.eye(n*2-1, dtype=int)
    baseflip = np.flip(base,axis=1)
    parts = np.split(base, base.shape[0])
    c = np.concatenate((baseflip[n-1:,:n-1], base[:n,:n]), axis=1)
    cflip = np.flip(c, axis = 0)
    res = np.concatenate((c, cflip[1:,:]))
    return np.array(res)

def main():
    print(diamond(5))

if __name__ == "__main__":
    main()

    # e=np.eye(n, dtype=int)
    # a=np.concatenate([e[::-1], e[:,1:]], axis=1)
    # result = np.concatenate([a[:-1], a[::-1]], axis=0)
    # return result