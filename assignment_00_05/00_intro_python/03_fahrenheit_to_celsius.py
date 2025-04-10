def main():
    
    input_fahrenheit = float(input("Enter a temperature in Fahrenheit:"))

    # Convert the input fahrenheit to celsius
    celsius = (input_fahrenheit - 32) * 5/9

    print(f"The temperature in Celsius is: {celsius :.2f}")


if __name__ == '__main__':
    main()