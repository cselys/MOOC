# Write your solution here:
from random import choice 

def  word_generator(characters: str, length: int, amount: int):
    return (getword(characters, length) for i in range(amount))

def getword(characters: str, n: int):
    return "".join([choice(characters) for i in range(n)])

if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)

# def word_generator(letters: str, length: int, amount:int):
#     return ("".join([choice(letters ) for i in range(length)]) for j in range(amount))