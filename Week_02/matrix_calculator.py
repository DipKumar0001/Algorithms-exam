def input_matrix(name):
    """Helper to input a matrix from user."""
    print(f"\n--- Enter Matrix {name} ---")
    try:
        rows = int(input(f"Enter number of rows for {name}: "))
        cols = int(input(f"Enter number of cols for {name}: "))
        
        matrix = []
        print(f"Enter the {rows}x{cols} values (one row per line, space separated):")
        for i in range(rows):
            row = list(map(float, input(f"Row {i+1}: ").strip().split()))
            if len(row) != cols:
                print(f"Error: Expected {cols} values.")
                return None
            matrix.append(row)
        return matrix
    except ValueError:
        print("Invalid input.")
        return None

def print_matrix(matrix):
    if not matrix:
        return
    for row in matrix:
        print(row)

def add_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Dimension Mismatch. Cannot Add."
    
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

def subtract_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Dimension Mismatch. Cannot Subtract."
    
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        result.append(row)
    return result

def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    if cols_A != rows_B:
        return f"Dimension Mismatch. {cols_A} != {rows_B}. Cannot Multiply."
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
                
    return result

def calculator():
    print("Welcome to Matrix Calculator")
    matrix_a = None
    matrix_b = None
    
    while True:
        # If matrices are not set, ask for them
        if matrix_a is None or matrix_b is None:
            matrix_a = input_matrix("A")
            if matrix_a is None: continue
            matrix_b = input_matrix("B")
            if matrix_b is None: continue
        
        print("\n--- Menu ---")
        print("1. Add (A + B)")
        print("2. Subtract (A - B)")
        print("3. Multiply (A * B)")
        print("4. Enter New Matrices")
        print("5. Quit")
        
        choice = input("Select Operation (1-5): ")
        
        if choice == '1':
            res = add_matrices(matrix_a, matrix_b)
            print("\nResult (A + B):")
            print_matrix(res)
        elif choice == '2':
            res = subtract_matrices(matrix_a, matrix_b)
            print("\nResult (A - B):")
            print_matrix(res)
        elif choice == '3':
            res = multiply_matrices(matrix_a, matrix_b)
            print("\nResult (A * B):")
            print_matrix(res)
        elif choice == '4':
            matrix_a = None
            matrix_b = None
            print("Resetting matrices...")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    calculator()
