
def get_name():
    """
    Returns the name of the user.
    """
    name = input("Enter your name: ")  # Prompt the user for their name
    return name  # Return the entered name

def greeting(name: str):
    """
    Prints a greeting message with the user's name.
    """
    print(f"Hello, {name}! Welcome!")  # Print a greeting message with the user's name

def main():
    """
    Main function to execute the program.
    """
    name = get_name()  # Get the user's name
    greeting(name)  # Print the greeting message

if __name__ == '__main__':
    main()  