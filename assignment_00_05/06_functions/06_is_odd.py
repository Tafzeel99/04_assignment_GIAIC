def main():
    lst = []  # Make an empty list to store integers
    user_input = input("Enter an integer or press enter to stop: ")  # Get user input for an integer
    while user_input != "":  # While the user doesn't press enter
        lst.append(int(user_input))  # Convert the input to an integer and add it to the list
        user_input = input("Enter an integer or press enter to stop: ")  # Prompt for the next input

    for value in lst:  # Loop through the list of integers
        if is_odd(value):  # Check if the value is odd
            print(f"{value} is odd")
        else:
            print(f"{value} is even")

def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns true.
    """
    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1



if __name__ == '__main__':
    main()