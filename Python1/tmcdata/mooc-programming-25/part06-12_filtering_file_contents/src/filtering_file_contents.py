# Write your solution here
def filter_solutions():
    with open("solutions.csv") as my_file:
        solutions = []
        for line in my_file:
            solutions.append(line.replace("\n","").split(";"))

    with open("correct.csv","w") as my_file:
        for row in solutions:
            print(row)
            if "+" in row[1]:
                nums = row[1].split("+")
                if int(nums[0]) + int(nums[1]) != int(row[2]):
                    continue
            elif "-" in row[1]:
                nums = row[1].split("-")
                if int(nums[0]) - int(nums[1]) != int(row[2]):
                    continue
            my_file.write(";".join(row) +"\n")

    with open("incorrect.csv","w") as my_file:
        for row in solutions:
            if "+" in row[1]:
                nums = row[1].split("+")
                if int(nums[0]) + int(nums[1]) == int(row[2]):
                    continue
            elif "-" in row[1]:
                nums = row[1].split("-")
                if int(nums[0]) - int(nums[1]) == int(row[2]):
                    continue
            my_file.write(";".join(row)+"\n")

    # with open("solutions.csv") as source, open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
    #     for row in source: