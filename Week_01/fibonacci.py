def iterative_fibonacci(n):
    """
    Calculates the first N Fibonacci numbers iteratively.
    Input: Integer N
    Output: List of integers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Initialize implementation
    fibs = [0, 1]
    
    # Loop from 2 to N-1
    for _ in range(2, n):
        next_val = fibs[-1] + fibs[-2]
        fibs.append(next_val)
        
    return fibs

if __name__ == "__main__":
    try:
        num = int(input("Enter N (number of Fibonacci terms): "))
        result = iterative_fibonacci(num)
        print(f"First {num} Fibonacci numbers: {result}")
    except ValueError:
        print("Please enter a valid integer.")
