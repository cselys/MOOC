#!/usr/bin/env python3

def extract_numbers(s):
    res = []
    for num in s.split():
        try:
            i = int(num)
            res.append(i)
        except Exception:
            try:
                f = float(num)
                res.append(f)
            except Exception:
                pass

    return res

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
