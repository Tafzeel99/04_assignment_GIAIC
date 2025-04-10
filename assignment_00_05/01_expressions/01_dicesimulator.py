import random

NUM_SIDES = 6

def roll_dice():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2

    print(f"Die 1: {die1} Die 2: {die2} Total of two dies: {total}")

def main():
    die1 = 10
    print("Die1 in main() starts with value:", die1)

    for _ in range(3):
        roll_dice()

        print("Die1 in main() is still:", die1)

if __name__ == "__main__":
    main()
# The code simulates rolling two dice and prints the result. and show block scope of variable.



