# this program show how the mutliple produce and write to 
# to one queue and multiple consumer can consume from one 
# queue 

import collections
import threading
import time
import random 

buffer = collections.deque(maxlen = 5)
condition = threading.Condition()

# method show a producer process 
def producer(thread_id): 
    print(f"Producer ID: {thread_id} trying to aquire the lock")
    for i in range(10): # trying to produce 10 items
        with condition: # Acquire the internal lock on condition variable 
            print(f"Producer ID: {thread_id} aquired the lock")
            while len(buffer) == buffer.maxlen:
                print(f"Producer ID {thread_id}: Buffer is full")
                condition.wait() # Release lock and wait for consumer to make space 
        
            item = f"item_{i}"
            buffer.append(item)
            print(f"Producer ID {thread_id} : Added item ${item}")
            condition.notify()
        time.sleep(0.2)

                        
def consumer(thread_id): 
    print(f"Consumer ID {thread_id}: trying to acquire lock")
    while True: 
        with condition: # Acquire the internal lock
            while not buffer: # while buffer is empty 
                print(f"Consumer: Buffer empty. Waiting...")
                condition.wait()

            item = buffer.popleft()
            print(f"Consumer ID {thread_id} consumed {item}, Buffer :{list(buffer)}")
            condition.notify() # Notify one waiting producer that space is available
        time.sleep(0.7)

if __name__ == "__main__":
    thread_1 = threading.Thread(target=producer, args=[1])
    thread_2 = threading.Thread(target=consumer, args=[1])

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print("Finished Producer and Consumer")


    



