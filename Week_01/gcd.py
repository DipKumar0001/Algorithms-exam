def recursive_gcd(x, y):
    """
    Calculates the Greatest Common Divisor (GCD) of x and y recursively.
    Based on Euclidean Algorithm.
    """
    if y == 0:
        return x
    return recursive_gcd(y, x % y)

if __name__ == "__main__":
    try:
        x_in = int(input("Enter first number (x): "))
        y_in = int(input("Enter second number (y): "))
        result = recursive_gcd(x_in, y_in)
        print(f"GCD of {x_in} and {y_in} is: {result}")
    except ValueError:
        print("Please enter valid integers.")
