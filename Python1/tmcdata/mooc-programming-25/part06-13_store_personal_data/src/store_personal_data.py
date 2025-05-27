# Write your solution here
def store_personal_data(person: tuple):
    with open("people.csv","a") as my_file:
        record = []
        for x in person:
            record.append(str(x))
        my_file.write(";".join(record))

