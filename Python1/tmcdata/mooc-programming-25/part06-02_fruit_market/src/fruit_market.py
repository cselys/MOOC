# write your solution here
def read_fruits():
    with open("fruits.csv") as new_file:
        result = {}
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            result[parts[0]] = float(parts[1])
        return result