# following files shows how semaphore can be used for peform the synchronization 
import threading
import types
import time
import random 


MAX_CONCURRENT_ACCESS = 3
resource_semaphone = threading.Semaphore(MAX_CONCURRENT_ACCESS)

def access_shared_resource(thread_id):
    print(f"{thread_id} trying to aquire the shared semaphone")

    resource_semaphone.acquire()

    try:
        print(f"Thread {thread_id} ***Acquired Resources, Accessing Now***")
        time_to_access = random.uniform(0.2, 0.5)
        time.sleep(time_to_access)
        print(f"Thread {thread_id} ***Finished accessing Resource in time ${time_to_access}***")
    finally:
        # Release the permit back to semapore 
        resource_semaphone.release()
        print(f"Thread {thread_id} ***Released Resource***")


if __name__ == "__main__":
    num_threads = 10 
    threads = []
    print(f"Starting {num_threads} threads, with max {MAX_CONCURRENT_ACCESS} concurrent resource access.")

    for i in range(num_threads):
        thread = threading.Thread(target=access_shared_resource, args=[i])
        threads.append(thread)
        thread.start()

    for thread in threads: 
        thread.join()

    print("\n all threads have completed their task")
        

        
