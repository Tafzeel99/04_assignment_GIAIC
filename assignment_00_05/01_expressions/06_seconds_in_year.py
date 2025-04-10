# Useful constants to help make the math easier and cleaner!
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    # Calculate the number of seconds in a year 
    seconds_in_year = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN

    # Prompt the user for input
    user_input_years = int(input("Enter a number of years: "))
    converted_seconds = user_input_years * seconds_in_year

    # Print the result
    print(f"There are {converted_seconds} seconds in {user_input_years} years.")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()