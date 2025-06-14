#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    print(a.shape)    
    return ((a.shape[0]-1)/2,(a.shape[1]-1)/2)   # note the order: (center_y, center_x)

def radial_distance(a):
    res = np.zeros((a.shape[0],a.shape[1]))
    cen = center(a)
    for row in range(a.shape[0]):
        for col in range(a.shape[1]):
            res[row,col] = np.sqrt((cen[0]-col) ** 2 + (cen[1] - row)**2)
    return res

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    amin = np.min(a)
    amax = np.max(a)
    if amax == amin:
        return np.full_like(a, tmax, dtype=float)  
    scaled_a = (a - amin) / (amax - amin) 
    return scaled_a * (tmax - tmin) + tmin

def radial_mask(a):
    distances = radial_distance(a)
    mask = scale(distances, 0.0, 1.0)
    return mask

def radial_fade(a):
    mask = radial_mask(a)
    return a * mask[:, :, np.newaxis]

def main():
    # a=np.zeros((1,1,3))
    # for n in range(1, 10):
    #     for m in range(1, 10):
    #         a=np.zeros((n, m, 3))
    #         rm = radial_mask(a)
    #         print(rm[(n-1)//2, (m-1)//2])
    # print(radial_distance(a))
    # print(radial_mask(a)[0,0])

    painting = plt.imread("src/painting.png")
    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(painting)
    ax[1].imshow(radial_mask(painting))
    ax[2].imshow(radial_fade(painting))
    plt.show()

if __name__ == "__main__":
    main()
