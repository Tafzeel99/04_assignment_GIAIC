import random 

NUM_SIDES = 6

# Simulate rolling a die
def main():
    die2 = random.randint(1, NUM_SIDES)
    die1 = random.randint(1, NUM_SIDES)
    # Calculate the total of the two dice
    total = die1 + die2

    print(f"""Die1 is: {die1}, 
Die2 is: {die2}, 
Total: {total}""")
    
if __name__ == "__main__":
    main()