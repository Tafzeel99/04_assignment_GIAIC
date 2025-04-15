def print_multiple(message: str, repeats: int): 
    """
    Prints the given message a specified number of times.
    """
    for i in range(repeats):  # Loop through the number of repeats
        print(message)  # Print the message

def main():
    """
    Main function to prompt the user for a message and the number of repeats,
    and then call print_multiple to display the message.
    """
    message = input("Please type a message: ")  # Prompt the user for a message
    repeats = int(input("Enter a number of times to repeat your message: "))  # Prompt for the number of repeats
    print_multiple(message, repeats)  # Call the function to print the message

if __name__ == '__main__':
    main()
