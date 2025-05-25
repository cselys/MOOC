# Write your solution here
my_list = []
addvalue = 1
while True:
    print("The list is now", my_list)
    op = input("a(d)d, (r)emove or e(x)it: ")
    if op == "x":
        break
    elif op == "d":
        my_list.append(addvalue)
        addvalue += 1
    elif op == "r":
        my_list.pop()
        addvalue -= 1
print("Bye!")