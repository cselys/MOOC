# Write your solution here
def find_words(search_term: str):
    with open("words.txt") as words_file:
        words = []
        results = []
        for line in words_file:
            words.append(line.replace("\n",""))
        if "." in search_term:
            for word in words:
                if len(word) == len(search_term):
                    found = True
                    for i in range(len(word)):
                        if search_term[i] != "." and search_term[i] != word[i]:
                            found = False
                            break
                    if found:
                        results.append(word)
        elif "*" in search_term:
            for word in words:
                if search_term.startswith("*") and word.endswith(search_term[1:]):
                    results.append(word)
                elif search_term.endswith("*") and word.startswith(search_term[:len(search_term)-1]):
                    results.append(word)                
        else:
            for word in words:
                if word == search_term:
                    results.append(word)
        return results