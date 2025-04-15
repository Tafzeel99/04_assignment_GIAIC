max_value = 100 

def main():
    curr_value = int(input("Enter a number: "))  # Ask the user to enter a number
    while curr_value < max_value:  
        curr_value *= 2  # Double the current value
        print(curr_value, end=" ") 
    print()  # Print a newline after the loop ends


if __name__ == '__main__':
    main()