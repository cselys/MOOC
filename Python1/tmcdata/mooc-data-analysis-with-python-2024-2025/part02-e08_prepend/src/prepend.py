#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, pre: str):
        self.pre = pre
    
    def write(self, seg: str):
        print(f"{self.pre}{seg}")

def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()
