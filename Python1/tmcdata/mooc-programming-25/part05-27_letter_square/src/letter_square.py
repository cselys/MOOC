# Write your solution here
def replace_elements(my_str: str, start: int, end: int, my_char:str):
    new_str =  my_str[:start] + my_char * (end - start - 1) + my_str[end - 1:]
    return new_str

layers = int(input("Layers:"))
width = layers * 2 - 1

letters = [chr(i) for i in range(ord('A'),ord('Z') + 1)]

base_row = letters[layers-1] * width
tops = [base_row] * layers
for i in range(1, layers):
    for j in range(i, layers):
        tops[j] = replace_elements(tops[j], i, width - i + 1 , letters[layers - i -1])

for i in range(0, width):
    if i < layers:
        print(tops[i])
    else:
        print(tops[width - i - 1])

