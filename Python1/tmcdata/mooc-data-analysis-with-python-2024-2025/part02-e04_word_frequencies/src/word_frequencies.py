#!/usr/bin/env python3

def word_frequencies(filename):
     with open(filename) as f:
        res = {}

        for line in f:
            s = line.replace('\n', '').split(" ")
            for word in s:
                word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if word not in res:
                    res[word] = 0
                res[word] += 1
        return res

def main():
    word_frequencies("alice.txt")

if __name__ == "__main__":
    main()


# with open(filename) as in_file:
#         for w in in_file.read().split():
#             ws = w.strip("""!"#$%&'()*,-./:;?@[]_""")
#             if ws not in result:
#                 result[ws] = 0
#             result[ws] += 1
#     return result