
def main():
    for i in range(10):
        for j in range(10):
            if j == 9:
                print('{:>4}'.format((i+1) * (j+1)))
            else:
                print('{:>4}'.format((i+1) * (j+1)), end='')

if __name__ == "__main__":
    main()
