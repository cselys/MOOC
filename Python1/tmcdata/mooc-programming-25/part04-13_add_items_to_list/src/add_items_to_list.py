# Write your solution here
items = []
count = int(input("How many items: "))
index = 0
while index < count:
    item = int(input(f"Item {index+1}"))
    items.append(item)
    index += 1
print(items)