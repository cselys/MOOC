# Write your solution here
def getnext(start):
    for i in range(2, start):
        if start % i == 0:
            return getnext(start+1)
    return start
        
def prime_numbers():
    start = 2
    while True:
        yield start
        start = getnext(start + 1)

if __name__=="__main__":
    numbers = prime_numbers()

    for i in range(8):
        print(next(numbers))

# def prime_numbers():
#     number = 1
#     while True:
#         if is_prime(number):
#             yield number
#         number += 1
