# Write your solution here
my_list = []
count = 0
while True:
    w = input("Word:")
    if w in my_list:
        print(f"You typed in {count} different words")
        break
    else:
        count += 1
        my_list.append(w)
