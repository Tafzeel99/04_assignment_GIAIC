def main():
    # Prompt the user for their weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ").lower()


    # Define the gravitational constants for each planet
    gravity_factors = {
        "mercury": 0.376,
        "venus": 0.889,
        "mars": 0.378,
        "jupiter": 2.36,
        "saturn": 1.081,
        "uranus": 0.815,
        "neptune": 1.14
    }

    # Check if the planet is in the dictionary and calculate the weight
    if planet in gravity_factors:
        planet_weight = round(earth_weight * gravity_factors[planet], 2)
        print(f"The equivalent weight on {planet}: {planet_weight}")
    else:
        print("Invalid planet name. Please enter a valid planet.")

if __name__ == "__main__":
    main()