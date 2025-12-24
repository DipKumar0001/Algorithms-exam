from collections import deque

def generate_binary_numbers(n):
    """
    Generates binary numbers from 1 to N using a Queue.
    Logic:
    1. Enqueue "1"
    2. Dequeue front, print it.
    3. Append "0" to front and Enqueue.
    4. Append "1" to front and Enqueue.
    """
    if n <= 0:
        return
    
    q = deque()
    q.append("1")
    
    result = []
    
    # We only want to find binary represention FOR the number N? 
    # Or generate the first N binary numbers?
    # The prompt implies generating a sequence or converting.
    # Standard algorithm generates first N binary numbers.
    
    for i in range(n):
        front = q.popleft()
        result.append(front)
        
        q.append(front + "0")
        q.append(front + "1")
        
    return result

if __name__ == "__main__":
    try:
        num = int(input("Enter N to generate first N binary numbers: "))
        bins = generate_binary_numbers(num)
        print(f"First {num} binary numbers: {bins}")
    except ValueError:
        print("Invalid integer.")
