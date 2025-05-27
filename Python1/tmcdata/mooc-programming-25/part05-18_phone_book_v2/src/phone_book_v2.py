# Write your solution here
d = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 3:
        print("quitting...")
        break
    else:
        name = input("name:")
        if command == 1:
            if name not in d:
                print("no number")
            else:
                for num in d[name]:
                    print(num)
        elif command == 2:
            number = input("number:")
            if name not in d:
                d[name] = []
            d[name].append(number) 
            print("ok!")
