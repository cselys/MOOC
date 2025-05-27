# Write your solution here
topics = []
with open("diary.txt", "r") as my_file:
    for line in my_file:
        topics.append(line.replace("\n", ""))

with open("diary.txt", "w") as my_file:    
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        command = int(input("Function:"))
        if command == 0:
            print("Bye now!")
            break
        elif command == 2:
            print("Entries:")
            for entry in topics:
                print(entry)
        elif command == 1:
            entry = input("Diary entry:")
            topics.append(entry)
            my_file.write(entry + "\n")
            print("Diary saved")