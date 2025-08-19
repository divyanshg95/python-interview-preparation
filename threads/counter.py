# this implement a thread safe counter which can be access 
# by only one thread at a time 


import threading
import time 
import random

lock = threading.Lock()
counter = 0 


# this is interesting to notice that we take a lock and return the values 
# while keeping the lock 
# you can implement similar logic using the acquire and release method 
def nextCounter(thread_id: int) -> int:
    print(f"{thread_id} requesting lock")
    global counter
    with lock:
        counter += 1
        print(f"{thread_id} incremented counter, value = {counter}")
        return counter
    

def task(thread_id):
    print(f"{thread_id} starting task..")
    random_time = random.uniform(0.1,0.8)
    time.sleep(random_time)
    nCounter = nextCounter(thread_id) 
    print(f"{thread_id} got counter {nCounter}")

if __name__ == "__main__":

    threads = []

    for i in range(10):
        thread = threading.Thread(target= task, args=(i,) )
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("All threads are finished")












