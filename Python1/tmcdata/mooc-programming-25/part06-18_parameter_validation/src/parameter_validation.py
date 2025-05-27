# Write your solution here
def new_person(name: str, age: int):
    try:
        message = ''
        if not name:
            message = "name is an empty string"
        elif len(name.split(" ")) < 2:
            message = "name contains less than two words"
        elif len(name)> 40:
            message = "name is longer than 40 characters"
        print(message)
        if message:
            raise ValueError(message)

        if not message:
            if age < 0:
                message ="age is a negative number"
            elif age > 150:
                message = "age is greater than 150"

        if message:
            raise ValueError(message)
    except:
        pass

    if not message:
        return(name,age)
    else:
        print(message)
        raise ValueError(message)


#  if name == "" or (" " not in name) or len(name) > 40:
#         raise ValueError("Invalid argument value for name: " + name)
 
#     # Validate age
#     if age < 0 or age > 150:
#         raise ValueError("Invalid argument value for age:" + str(age))
 
#     # Both ok
#     return (name, age)