# Write your solution here
from string import ascii_uppercase

# def get_commands(program:list, jumpto:str):
#     if jumpto == "":
#         return program
#     else:
#         return program

def run(program: list):
    result = []
    var_dict = {}
    command = ""
    while command != "END":
        commands = program #get_commands(program, "")
        for c in commands:
            c_split = c.split(" ")
            if c_split[0] == "MOV":
                var_dict[c_split[1]] = int(c_split[2])
            elif c_split[0] == "PRINT":
                if c_split[1] not in var_dict.keys():
                    var_dict[c_split[1]] = 0
                result.append(var_dict[c_split[1]])
            elif c_split[0] == "ADD":
                if c_split[2] in ascii_uppercase:
                    var_dict[c_split[1]] += var_dict[c_split[2]]
                else:
                    var_dict[c_split[1]] += int(c_split[2])
            elif c_split[0] == "SUB":
                if c_split[2] in ascii_uppercase:
                    var_dict[c_split[1]] -= var_dict[c_split[2]]
                else:
                    var_dict[c_split[1]] -= int(c_split[2])
            elif c_split[0] == "MUL":
                if c_split[2] in ascii_uppercase:
                    var_dict[c_split[1]] *= var_dict[c_split[2]]
                else:
                    var_dict[c_split[1]] *= int(c_split[2])                                
            elif c_split[0] == "END":                 
                command = "END"
            else:
                command = "END"
    return result
