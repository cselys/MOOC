# Write your solution here
my_list = []
while True:
    num = int(input("New item:"))
    if num == 0:
        break
    else:
        my_list.append(num)
        print("The list now:", my_list)
        print("The list in order:", sorted(my_list))
print("Bye!")