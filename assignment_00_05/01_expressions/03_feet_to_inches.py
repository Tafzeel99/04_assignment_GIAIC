# that converts feet to inches.
INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches in 1 foot.

def main():
    feet: float = float(input("Enter number of feet: "))
    inches: float = feet * INCHES_IN_FOOT  # Perform the conversion
    print(f"That is {inches: .2f} inches!")
    
if __name__ == '__main__':
    main()