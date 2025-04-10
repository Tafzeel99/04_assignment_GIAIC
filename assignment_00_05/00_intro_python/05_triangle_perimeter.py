def main():
    
    side_a : float = float(input("Enter the length of triangle side a:"))
    side_b : float = float(input("Enter the length of triangle side b:"))
    side_c : float = float(input("Enter the length of triangle side c:"))

    # Calculate the perimeter of the triangle
    perimeter = side_a + side_b + side_c

    print(f"The perimeter of the triangle is: {perimeter:.2f}")

if __name__ == '__main__':
    main()