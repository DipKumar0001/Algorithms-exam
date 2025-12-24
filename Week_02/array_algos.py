def find_max_min(arr):
    """
    Task 1: Find Max and Min values in a numerical array.
    """
    if not arr:
        return None, None
    
    local_max = arr[0]
    local_min = arr[0]
    
    for num in arr[1:]:
        if num > local_max:
            local_max = num
        if num < local_min:
            local_min = num
            
    return local_max, local_min

def bubble_sort(arr):
    """
    Task 2: Sort elements of a list using Bubble Sort.
    """
    n = len(arr)
    # Create a copy to avoid modifying original if needed
    sorted_arr = arr.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    return sorted_arr

def shift_zeros_left(arr):
    """
    Task 3: Create a new list shifting all zeros to the left.
    """
    zeros = [x for x in arr if x == 0]
    non_zeros = [x for x in arr if x != 0]
    return zeros + non_zeros

if __name__ == "__main__":
    # Test Data
    sample_list = [5, 0, 12, -3, 0, 8, 1, 0, 9]
    print(f"Original List: {sample_list}")
    
    # Task 1
    mx, mn = find_max_min(sample_list)
    print(f"Max: {mx}, Min: {mn}")
    
    # Task 2
    sorted_list = bubble_sort(sample_list)
    print(f"Sorted List: {sorted_list}")
    
    # Task 3
    shifted_list = shift_zeros_left(sample_list)
    print(f"Zeros Shifted Left: {shifted_list}")
