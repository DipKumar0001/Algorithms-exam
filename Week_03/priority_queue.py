class PriorityQueue:
    """
    Simple Priority Queue implementation using a list.
    Elements are sorted upon insertion (or processed to find min on pop).
    Requirement: Latin letters, priority = alphabetical order.
    """
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)
        # Sort to maintain priority order (Smallest/First Alphabet at index 0)
        # O(N log N) - efficient enough for this lab scope
        self.queue.sort() 

    def pop(self):
        if self.is_empty():
            return "Queue is empty"
        # Since we sorted, index 0 is the highest priority (e.g., 'a')
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return str(self.queue)

if __name__ == "__main__":
    pq = PriorityQueue()
    chars = ['r', 'y', 'd', 'a', 'h']
    print(f"Adding chars: {chars}")
    for c in chars:
        pq.push(c)
    
    print(f"Queue state: {pq}")
    
    print("\nPopping elements:")
    while not pq.is_empty():
        print(f"Popped: {pq.pop()} | Remaining: {pq}")
