# Following program shows the Producer consumer scenario with multiple producer 
# and multiple consumers 
# it uses the mutex to protect the fixed size shared buffer and spin lock to keep 
# check if data is available 

#import deque 
from collections import deque
import time 
from threading import Lock, Thread 

# shared buffer of length 5
d = deque(maxlen=5)
# Lock protects the concurrent access on shared buffer by multiple threads
lock = Lock()

def producer(thread_id): 
    # produce 10 items 
    for i in range(5): 
        while True: 
            if lock.acquire(blocking= True):    
                try: 
                    if len(d) < d.maxlen:
                        item = f"item_{i}"
                        print(f"Producer {thread_id}: adding item in buffer {item}")
                        d.append(item)
                        break
                finally:
                    lock.release()
            else:
                print(f"Producer {thread_id}: buffer is full, going in sleep state")
                time.sleep(0.2)
        
                
def consumer(thread_id):
    #consume 5 items 
    while True: 
        print(f"Consumer {thread_id}: trying to acquire lock") 
        if lock.acquire(blocking=True):
            try:
                if len(d) > 0:
                    item = d.popleft()
                    print(f"Consumer {thread_id}: consumed item {item}")
                else:
                    print(f"Consumer {thread_id}: buffer is empty")
            finally:
                lock.release()
        time.sleep(0.5)


if __name__ == "__main__":

    producers = []
    consumers = []

    for i in range(3):
        producers.append(Thread(target=producer, args=(i,)))
        consumers.append(Thread(target=consumer, args=(i,)))
    
    for i in range(3):
        consumers[i].start()
        producers[i].start()


    for p in producers:
        p.join()
    for c in consumers:
        c.join()

    


            

