import sys


#This file contains the heap implementation which is implemented 
#from scratch without using any builtin library 




class MinHeap:
    def __init__(self) -> None:
        self.heap = []
        self.heap_size = 0 
        self.capacity = 10 
    
    def parent(self, i) -> int:
        return (i-1) / 2
    
    def left(self, i) -> int: 
        return 2*i + 1
    
    def right(self, i) -> int: 
        return 2*i + 2
    
    # swap the values present at i and j indexes
    def swap(self, i,j) -> None:
        t = self.heap[i]
        self.heap[i]  = self.heap[j]
        self.heap[j] = t

    def insert(self, i, val) -> int: 
        if self.heap_size == self.capacity-1:
            raise Exception("Overflow")
        else:
            i = self.heap_size
            self.heap[self.heap_size] = val 
            self.heap_size += 1 
            while i !=0 & self.heap[self.parent(i)] > self.heap[i]:
                self.swap(self.parent(i), i)
                i = self.parent(i)



    def decreaseKey(self, i, val) -> None:
        self.heap[i] = val 
        while i != 0 & self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def extractMin(self) -> int:
        if self.heap_size == 0:
            return sys.maxsize
        elif self.heap_size == 1: 
            val = self.heap[0]
            self.heap_size -= 1
            return val 
        else: 
            val = self.heap[]
         
        
    def minHeapify(self, i) -> None:
        left = self.left(i)
        right = self.right(i)
        smallest = i
        if (left < self.heap_size & self.heap(smallest) > self.heap(left)):
            smallest = left 
        elif (right < self.heap_size & self.heap(smallest) > self.heap(right)):
            smallest = right
        
        if smallest != i: 
            self.swap(i, smallest)
            self.minHeapify(smallest)
    


            


         

