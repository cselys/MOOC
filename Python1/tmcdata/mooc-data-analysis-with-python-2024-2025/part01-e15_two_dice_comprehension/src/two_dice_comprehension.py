#!/usr/bin/env python3

def main():
    L = [(a,b) for a in range(1,7)
                 for b in range(1,7)
                 if a+b == 5]
    for x in L:
        print(x)
if __name__ == "__main__":
    main()


#   print("\n".join(f"({a},{b})" for a in range(1, 7) for b in range(1, 7) if a + b == 5))