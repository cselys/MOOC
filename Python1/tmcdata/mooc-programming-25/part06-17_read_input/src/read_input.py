# Write your solution here
def read_input(message: str, num1: int, num2: int):
    while True:
        try:
            input_str = input(message)
            number = int(input_str)
            if number >= num1 and number <= num2:
                return number
        except ValueError:
            pass
        print(f"You must type in an integer between {num1} and {num2}")
