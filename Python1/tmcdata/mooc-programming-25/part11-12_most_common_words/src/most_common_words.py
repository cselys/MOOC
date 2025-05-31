# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    with open(filename) as my_file:
        mydict = {}
        for line in my_file:            
            words = line.replace("\n","").replace(".","").replace(",", "").split(" ")
            mydict.update({word: mydict[word]+words.count(word) if word in mydict else words.count(word) for word in words})
        return {key: value for key, value in mydict.items() if value >= lower_limit}

if __name__=="__main__":
    most_common_words("programming.txt", 4)



# from string import punctuation
 
# def most_common_words(filename: str, lower_limit: int):
#     with open(filename) as f:
#         content = f.read()
 
#         # remove line breaks and punctuation
#         content = content.replace("\n", " ")
#         for punctuation_mark in punctuation:
#             content = content.replace(punctuation_mark, "")
 
#         words = content.split(" ")
#         return {word: words.count(word) for word in words if words.count(word) >= lower_limit}