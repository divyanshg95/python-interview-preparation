class ListQueue: 
    #This class provide a queue which is implemented using the 
    #python list 
    #performance of such queue is not very very good as remove 
    #of items at the beggining of the items is not very fast
    #as it has to shift all the elements 
    def __init__(self, size) -> None:
        self.size = size
        self.queue = []
    
    def enqueue(self, value) -> None:
        
    