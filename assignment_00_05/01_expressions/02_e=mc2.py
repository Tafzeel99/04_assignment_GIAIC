C: int = 299792458  # The speed of light in m/s

def main():
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy
    # equivalently energy = mass * (C ** 2)
    # using the ** operator to raise C to the power of 2
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display work to the user
    print("Formula: e = mC2")
    print("M stands for mass: m = " + str(mass_in_kg) + " kg")
    print("C stands for speed of light: C = " + str(C) + " m/s")
    
    print("joules of energy! = " + str(energy_in_joules))



if __name__ == '__main__':
    main()