def print_divisors(num: int):
    """
    Prints all divisors of the given number.
    """
    print("Here are the divisors of", num)  # Inform the user about the divisors being printed
    for i in range(num):  # Loop through numbers from 1 to num
        curr_divisor = i + 1  # Current number to check as a divisor
        if num % curr_divisor == 0:  # Check if the current number divides num without a remainder
            print(curr_divisor)  # Print the divisor

def main():
    """
    Main function to take user input and print divisors of the number.
    """
    num = int(input("Enter a number: "))  # Prompt the user to enter a number
    print_divisors(num)  # Call the function to print divisors of the entered number


# Entry point of the program
if __name__ == '__main__':
    main()