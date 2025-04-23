    #This class provide a queue which is implemented using the 
    #python list 
    #performance of such queue is not good as removal 
    #of items at the beggining of the items is not very fast
    #as it has to shift all the elements 
class ListQueue: 
    def __init__(self, size) -> None:
        self.size = size
        self.queue = []
    
    # add element at the end of the queue
    def push(self, value) -> None:
        if len(self.queue) < self.size:
            self.queue.append(value)
        else:
            raise OverflowError("Queue is full")

    # remove element from the front 1
    def pop(self) -> int:
        if len(self.queue) > 0:
            b = self.queue.pop(0)
            #self.queue[1:0] # slicing create a new list 2nd element onward and return that 
            # best option is to use the dequeue if you want to append and pop quickly 
            return b
        else:
            raise Exception("Queue is empty")

    #return the first element from the queue
    def front(self) -> int:
        if not self.isEmpty:
            a = self.queue[0]
            print(a)
            return a
        else:
            raise Exception("Queue is Empty")

    def rear(self) -> int:
        if not self.isEmpty:
            # There are many ways we can get the last element of the list 
            #a = self.queue.pop() pop cannot be used as it will remove the element from front
            b = self.queue[len-1]
            c = self.queue[-1] #negative index show the last element
            print(b)
            print(c)
            return b
            #sclicing check that method 
        else: 
            raise Exception("Queue is empty")

    def isFull(self) -> bool:
        return len(self.queue) == self.size

    def isEmpty(self) -> bool:
        return len(self.queue) < self.size
    
    def __str__(self) -> str:
        s = ""
        for c in self.queue:
            s = s + " " + str(c)
        return s + "\n"
        



def main():
    q = ListQueue(5)
    q.push(10)
    q.push(12)
    q.push(14)
    q.push(20)
    q.push(22)
    try:
        q.push(24)
    except:
        print("Queue is full")

    print(q)
    q.pop()
    print(q)
    q.pop()
    print(q)
    q.pop()
    print(q)
    q.pop()
    print(q)
    q.pop()
    print(q)
    

if __name__ == "__main__":
    main()