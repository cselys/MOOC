# write your solution here
with open("wordlist.txt") as new_file:
    wordlist = []
    for line in new_file:
        wordlist.append(line.strip())

    sentense = input("Write text:")
    result = ""
    for word in sentense.split(" "):
        if result != "":
            result += " "
        if word.lower() in wordlist:
            result += word
        else:
            result += "*"+word+"*"
    print(result)
