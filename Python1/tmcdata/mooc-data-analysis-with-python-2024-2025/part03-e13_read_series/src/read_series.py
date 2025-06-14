#!/usr/bin/env python3
import pandas as pd

def read_series():
    data = {}
    while True:
        line = input()
        if line.strip() == "":
            break

        parts = line.strip().split()
        if len(parts) != 2:
            raise ValueError(f"Malformed input line: '{line}'")

        index, value = parts
        data[index] = value

    return pd.Series(data, dtype=object)

def main():
    print(read_series())

if __name__ == "__main__":
    main()


# def read_series():
#     values=[]
#     indices=[]
#     while True:
#         line = input("")
#         if not line:
#             break
#         i, v = line.split()
#         values.append(v)
#         indices.append(i)
#     s = pd.Series(values, index=indices)
#     return s