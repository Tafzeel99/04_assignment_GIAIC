def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:  # Check if n is within the range [low, high], and operators are checked both left to right
        return True
    return False  # Return False if n is not in the range

if __name__ == "__main__":
    # Test the function with some examples
    print(in_range(5, 1, 10))  # True
    print(in_range(0, 1, 10))  # False
    print(in_range(10, 1, 10))  # True
    print(in_range(11, 1, 10))  # False