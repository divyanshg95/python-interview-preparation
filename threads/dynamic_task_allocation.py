import threading 
import time 
import queue


# In Python the target function mapping for a thread happens at the 
# time the time of Thred object creation. To dynamically assign task to 
# thread we need to use the task queue 
# follow program demontrate the use the use of the queue 
# 
# The Thread is in running state 
# It is continuously pooling it's task queue 
# User can submit a task, it will pick up task sequentially and finish that 

class DynamicThread(threading.Thread):
    def __init__(self, group = None, target = None, name = None, args = ..., kwargs = None, *, daemon = None):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.task_queue = queue.Queue()
        self.shutdown_event = threading.Event() # event is set to shut down the the thread pool
        self.start() # this will immediately start the thread


    def run(self):
        print(f"Thread {self.name} started")
        while not self.shutdown_event.is_set(): # Keep running until shutdown single received
            try: 
                task_function, args, kargs = self.task_queue.get(timeout=1) # Get a task from queue with timeout
                print(f"Thread {self.name} starting task {task_function.__name__}")
                task_function(*args, **kargs)
                self.task_queue.task_done()

            except queue.Empty:
                print(f"Thread {self.name}, Queue is empty at {time.strftime('%Y-%m-%d %H:%M:%S')}, moving to idle state")
                pass
            
        print(f"Thread {self.name} finished")

    def assign_task(self, func, *args, **kargs):
        """Dynamically assign a new function to executed by Thread """
        self.task_queue.put((func,args, kargs))

    def stop(self):
        """Singal the Thread to Shutdown"""
        self.shutdown_event.set()
        self.join() # Wait for thread to finish

#Example Task 
def task_a(message): 
    print(f" Task A, {message}")
    time.sleep(0.2)
    print(f"Finished Task A")

def task_b(num1, num2): 
    print(f" Task B, Sum ={num1 + num2}")
    time.sleep(0.5)
    print(f"Finished Task B")

def task_c(name):
    print(f" Task C, Hello = {name}")
    time.sleep(0.5)
    print(f"Finished Task C")


if __name__ == "__main__":
    dt = DynamicThread(name="DynamicThread")

    # Assign task 
    dt.assign_task(task_a, "First Message")
    dt.assign_task(task_b, 10, 20)
    dt.assign_task(task_c, "Alice")
    dt.assign_task(task_a, "Second Message")

    dt.task_queue.join()

    print("All Submited task are done")
    dt.assign_task(task_c, "Alice")

    time.sleep(10)
    
    dt.stop()


