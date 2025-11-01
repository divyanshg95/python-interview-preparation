# Semaphore are used for access control and synchronisation 
# They don't have any ownership 
# Python provide simple API calls for acquire and release the locks 


from  threading import Semaphore, Thread
import time 
import counter
import random


NUMBER_OF_CONCURRENT = 3
semaphore = Semaphore(3)


# Method behaves as the shared resource 
def print_shared(thread_id):
    print(f"Thread {thread_id} trying to access the shared resouce")
    try: 
        if semaphore.acquire(True):
            print(f"Thread: {thread_id} accessing the shared resource")
            time.sleep(random.uniform(0.2,3))
    finally:
        print(f"Thread: {thread_id} releasing the shared resource")
        semaphore.release()

if __name__ == "__main__":
    threads = []
    for i in range(20):
        threads.append(Thread(target=print_shared, args= (i,)))
    
    for t in threads:
        t.start()

    for t in threads:
        t.join()





    
        


            
    



