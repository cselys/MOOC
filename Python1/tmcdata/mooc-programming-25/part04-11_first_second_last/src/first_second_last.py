# Write your solution here
def first_word(mystr):
    spaceat = mystr.find(" ")
    return mystr[:spaceat]

def second_word(mystr):
    space1at = mystr.find(" ")
    space2at = mystr[space1at+1:].find(" ")
    if space2at < 0:
        return mystr[space1at+1:]
    return mystr[space1at+1:space1at+1+space2at]

def last_word(mystr):
    last = mystr.find(" ")
    while last >= 0:
        mystr = mystr[last+1:]
        last = mystr.find(" ")              
    return mystr

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))