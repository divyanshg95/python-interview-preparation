# Generally the counter example are implemeneted such their is global counter 
# each thread comes and increment the counter 
# In following implementation counter is separate class which have the class method 
# getNext which will increment the counter and return it's value 
# this is thread safe implementation which means that their will not be race conditions

from threading import Lock, Thread 
import time

class Counter: 
    lock = Lock()
    counter = 0 


    @classmethod
    def getNext(cls): 
        with cls.lock:
            time.sleep(1)
            cls.counter += 1
            return cls.counter 
    

def print_target(thread_id) : 
    c = Counter.getNext()
    print(f"Thread {thread_id} got counter {c}")



if __name__ == "__main__":
    # create 10000 thread, each thread will fetch the counter 
    # in print on console 

    threads = []
    for i in range(500):
        threads.append(Thread(target=print_target, args=(i,)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(f"Final counter value {Counter.counter}")
    
        


    