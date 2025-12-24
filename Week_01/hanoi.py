def tower_of_hanoi(n, source, destination, auxiliary):
    """
    Solves Tower of Hanoi problem recursively.
    Input: n (disks), source, destination, auxiliary (rod names)
    Output: Prints moves
    """
    if n <= 0:
        return
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n-1, source, auxiliary, destination)
    
    # Move nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n-1, auxiliary, destination, source)

if __name__ == "__main__":
    try:
        num = int(input("Enter number of disks (N): "))
        print(f"\nSteps to solve for {num} disks:")
        # Standard rods: A (Source), C (Destination), B (Auxiliary)
        tower_of_hanoi(num, 'A', 'C', 'B')
        print(f"\nTotal moves: {2**num - 1}")
    except ValueError:
        print("Please enter a valid integer.")
