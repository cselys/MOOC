#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    with open(filename) as f:
        res = []
        i = 0
        for line in f:
            if i == 0:
                i = 1
                continue
            mo = re.search(r'([0-2]?[0-9]?[0-9]+)\s*([0-2]?[0-9]?[0-9]+)\s*([0-2]?[0-9]?[0-9]+)\s*([a-zA-Z0-9]*\s?[a-zA-Z0-9]*)',line)
            if mo:
                res.append("\t".join(mo.groups()))    
        return res


def main():
    red_green_blue("rgb.txt")
    # print(red_green_blue("rgb.txt"))

if __name__ == "__main__":
    main()


    # with open(filename) as in_file:
    #     l = re.findall(r"(\d+)\s+(\d+)\s+(\d+)\s+(.*)\n", in_file.read())
    #     return [
    #         "{}\t{}\t{}\t{}".format(r, g, b, name)
    #         for r, g, b, name
    #         in l
    #     ]