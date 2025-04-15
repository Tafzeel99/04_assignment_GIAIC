def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        while True:
            try:
                amount_bought = input(f"How many ({fruit_name}) do you want to buy?: ")
                if amount_bought == "":  # If the user presses Enter without input
                    amount_bought = 0  # Assume they don't want to buy any
                amount_bought = int(amount_bought)
                break
            except ValueError:
                print("Please enter a valid number.")
        
        total_cost += (price * amount_bought)
    
    print("Your total is $" + str(total_cost))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()