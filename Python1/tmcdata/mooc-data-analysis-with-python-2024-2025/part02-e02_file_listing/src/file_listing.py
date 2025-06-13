#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    with open(filename) as f:
        res = []
        for line in f:
            mo = re.search(r'\s*(\d+)\s* ([A-Z][a-z][a-z])\s*([123]?[0-9]) ([0-2][0-9]):([0-5][0-9]) ([a-zA-Z-0-9_.]*.[a-z]+)' ,line)
            res.append((int(mo.group(1)), mo.group(2), int(mo.group(3)), int(mo.group(4)), int(mo.group(5)), mo.group(6)))
        return res

def main():
    print(file_listing("listing.txt"))

if __name__ == "__main__":
    main()

# (.+)