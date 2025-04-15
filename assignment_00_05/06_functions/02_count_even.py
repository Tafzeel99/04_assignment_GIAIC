def count_even(lst):
    """
    Returns number of even numbers in list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    count = 0  # Stores the count of even numbers in the list
    for num in lst:  # Loop through the numbers in the list
        if num % 2 == 0:  # Check if the number is even
            count += 1  # Increment the count for even numbers
    print(count)  # Print the total count of even numbers

def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []  # Make an empty list to store integers
    user_input = input("Enter an integer or press enter to stop: ")  # Get user input for an integer
    while user_input != "":  # While the user doesn't press enter
        lst.append(int(user_input))  # Convert the input to an integer and add it to the list
        user_input = input("Enter an integer or press enter to stop: ")  # Prompt for the next input
    return lst

def main():
    lst = get_list_of_ints()  # Get the list of integers from the user
    count_even(lst)  # Count and print the number of even numbers in the list

if __name__ == '__main__':
    main()