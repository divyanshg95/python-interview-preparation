# in python you can use the heapq module to implement heaps
# by default heapq module implements a min heap in order to use the max heap 
# you can use the negative values 

import heapq
from typing import List, Tuple, Any
from random import randint

# add the values in a heap 
my_heap =  []
for i in range(10, 0, -1):
    heapq.heappush(my_heap, i)
print(my_heap) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for _ in range(len(my_heap)):
    print(heapq.heappop(my_heap), end= ", ") # 1 2 3 4 5 6 7 8 9 10
print()

my_heap_1 = [2,35,5,6,9,10]
heapq.heapify(my_heap_1)
print("smallest element %d" % my_heap_1[0])


# you can store the objects in heap but you have to define 
# __lt__ method in the class. heapq module relies on this 
# comparison method to compare the objects in the heap. 


class Task:
    def __init__(self, name:str, priority:int) -> None:
        self.name = name 
        self.priority = priority
    
    def __lt__(self, other:Any) -> bool:
        return self.priority < other.priority
    
    def __repr__(self):
        return f"{self.name} with proirity {self.priority}"
    
def main():
    task = []
    for i in range(10):
        t = Task(f"Task {i}", randint(1, 10))
        print(f"appending task {t}")
        task.append(t)

    print("Before heapify")
    for i in task:
        print(i)
    print()

    heapq.heapify(task)
    print("After heapify")

    print("Popping tasks")
    for i in range(len(task)):
        print(heapq.heappop(task))
    print()

    print("After popping tasks")
    for i in task:
        print(i)
    print()
    print("Popping tasks")
    for i in range(len(task)):
        print(heapq.heappop(task))
    print()
    

    


if __name__ == "__main__":
    main()
