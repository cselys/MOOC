# Write your solution here
def get_dict(filename: str):
    with open(filename) as new_file:
        wholefile = []
        dictionary = {}
        for line in new_file:
            wholefile.append(line.replace("\n", ""))
        rec = []
        for item in wholefile:
            if not item and rec:
                dictionary[rec[0]] = rec[1:]
                rec = []
                continue
            rec.append(item)
        dictionary[rec[0]] = rec[1:]
        return dictionary

def search_by_name(filename: str, word: str):
    dictionary = get_dict(filename)
    res = []
    for topic in dictionary.keys():
        if word in topic.lower():
            res.append(topic)
    return res

def search_by_time(filename: str, prep_time: int):
    dictionary = get_dict(filename)
    res = []
    for item, value in dictionary.items():
        if int(value[0]) <= prep_time:
            res.append(f"{item}, preparation time {value[0]} min")
    return res
