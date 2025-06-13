#!/usr/bin/env python3

def reverse_dictionary(d):
    res = {}
    for key, value in d.items():
        for val in value:
            if val not in res:
                res[val] = []
            res[val].append(key)
    return res

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
