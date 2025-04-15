def main():
    curr_value = int(input("Enter a number: "))  # Ask the user to enter a number
    while curr_value < 100:  # Continue doubling while the value is less than 100
        curr_value *= 2  # Double the current value
        print(curr_value, end=" ")  # Print the doubled value on the same line
    print()  # Print a newline after the loop ends

if __name__ == '__main__':
    main()