#!/usr/bin/env python3

def detect_ranges(L):
    res = []
    start, end = 0, 0
    Ls = sorted(L)
    Ls.append(max(L) + 100)
    for index in range(len(L)):
        if Ls[index] + 1 == Ls[index+1]:
            end += 1
        else:
            if start == end:
                res.append(Ls[index])
            else:
                res.append((Ls[start], Ls[end]+1))
                
            start, end = index + 1, index + 1
    print(res)
    return res

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    # L = [-2, 0, 1, 2, 3]
    # L = [1, 2, 4]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
