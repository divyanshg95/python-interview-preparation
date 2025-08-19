from threading import Lock
from typing import Optional
from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()
        self.lock = Lock()

    def size(self) -> int: 
        with self.lock:
            return len(self.q)

    def enqueue(self, value: int) -> bool: 
        with self.lock:
            self.q.append(value)
            return True

    # Returns None if queue is empty
    def dequeue(self) -> Optional[int]: 
        with self.lock:
            if self.q:
                return self.q.popleft()
            return None

if __name__ == "__main__":
    print("Executing Main Function")
    print("Creating Queue")
    q = Queue()
    for i in range(1,  100001):
        q.enqueue(i)
    for i in range(1,  100001):
        q.dequeue()
    print(q.size())


# follow up question 
# can you make query a limited size 
