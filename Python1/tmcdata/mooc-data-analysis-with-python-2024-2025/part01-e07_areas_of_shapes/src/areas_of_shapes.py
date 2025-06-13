#!/usr/bin/env python3

import math

def main():
    # enter you solution here
    while True:
        choice = input("Choose a shape (triangle, rectangle, circle): ")
        area = 0
        if choice == 'triangle':
            base = int(input("Give base of the triangle: "))
            height = int(input("Give height of the triangle: "))
            area = base * height / 2
        elif choice == 'rectangle':
            width = int(input("Give width of the rectangle: "))
            height = int(input("Give height of the rectangle: "))
            area = width * height
        elif choice == 'circle':
            radius = int(input("Give radius of the circle: "))   
            area = math.pi * radius * radius   
        elif choice == '': 
            break
        else:
            print('Unknown shape!')
            continue
        print(f"The area is {area:.6f}")

if __name__ == "__main__":
    main()
