def main():
    lst = []  # Make an empty list to store things in

    value = input("Enter a value: ")  # Get an initial value
    while value:  # While the user input isn't an empty value
        lst.append(value) # Add val to list
        value = input("Enter a value: ")  # Get the next value to add

    print("Here's the list:", lst)



if __name__ == '__main__':
    main()