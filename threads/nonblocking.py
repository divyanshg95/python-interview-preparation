# Non-blocking thread locks 
# Following example show how a python program can aquire a non-blocking
# thread locks 
#  

import threading 
import time 
import random 

class Resource:
    def __init__(self):
        self.value = 0 
        self.lock = threading.Lock()

    def access_resource(self, thread_name: str) -> None:
        if self.lock.acquire(blocking=False):
            try: 
                print(f"{thread_name} acquired lock, Modifying resources")
                self.value += 1
                time.sleep(random.uniform(0.1, 0.5)) # Simulate work 
                print(f"{thread_name} finished, Resource value: {self.value}")
            finally:
                self.lock.release()
        else:
            print(f"{thread_name} failed to aquice lock, Skipping")

def worker(resource: Resource, thread_name: str):
    for _ in range(3):  # Try to access resource multiple times
        resource.access_resource(thread_name)
        time.sleep(random.uniform(0.1, 0.3)) #stimutale other work 

if __name__ == "__main__":
    resource = Resource()
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(resource, f"Thread={i}"))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final resource value: {resource.value}")
    


