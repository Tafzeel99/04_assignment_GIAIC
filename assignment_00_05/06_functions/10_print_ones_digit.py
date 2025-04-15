def print_ones_digit(num):
    """
    Prints the ones digit of the given number.
    """
    print("The ones digit is", num % 10)

def main():
    """
    Main function to prompt the user for a number and print its ones digit.
    """
    num = int(input("Enter a number: "))  # Prompt the user for a number
    print_ones_digit(num)  # Call the function to print the ones digit

if __name__ == '__main__':
    main()