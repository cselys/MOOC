# Write your solution here
from random import choice

def words(n: int, beginning: str):
    with open("words.txt") as my_file:
        words = []
        res = []
        for line in my_file:
            word = line.strip()
            if word.startswith(beginning):
                words.append(word)
        if len(words) < n:
            raise ValueError("not enough words") 
        
        while len(res) < n:
            w = choice(words)
            if w not in res:
                res.append(w)
        return res
