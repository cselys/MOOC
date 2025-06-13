#!/usr/bin/env python3
import sys

def file_extensions(filename):
    with open(filename) as f:
        res1 = []
        res2 = {}
        for line in f:
            line = line.strip('\n')
            if "." not in line:
                res1.append(line)
            else:
                segs = line.split(".")
                if segs[len(segs) - 1] not in res2:
                    res2[segs[len(segs) - 1]] = []
                res2[segs[len(segs) - 1]].append(line)
    return (res1, res2)

def main():
    res = file_extensions(sys.argv[1])
    if res:
        print(f"{len(res[0])} files with no extension")
        for key, value in sorted(res[1].items()):
            print(f"{key} {len(value)}")

if __name__ == "__main__":
    main()
