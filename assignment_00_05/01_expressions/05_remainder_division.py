def main():
    dividend = int(input("Enter the dividend to be divided: "))
    divisor = int(input("Enter the divisor to divide by: "))

    quotient = dividend // divisor
    remainder = dividend % divisor

    print(f"The divided value is: {quotient} with a remainder of {remainder}")

if __name__ == "__main__":  
    main()
# The code above calculates the quotient and remainder of a division operation.