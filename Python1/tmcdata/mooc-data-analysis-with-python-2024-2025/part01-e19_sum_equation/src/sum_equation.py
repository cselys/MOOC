#!/usr/bin/env python3

def sum_equation(L):
    if not L:
        return '0 = 0'
    if len(L) < 1:
        return f'{L[0]} = {L[0]}'
    res = f'{L[0]} ' 
    for i in range(1,len(L)):
        res += f'+ {L[i]} '
    res += f'= {sum(L)}'
    return res

def main():
    print (sum_equation([1,5,7]))

if __name__ == "__main__":
    main()

# result = list(map(str, L))
# return " + ".join(result) + f" = {sum(L)}"