#Design 
# 3 User Threads - They are submitting the jobs at random internalvals 
# Each Job object object hold the time value which specifies the Time Taken to 
# finish that job 
# 
# ThreadPool Takes number n which will be the number of threads available in 
# Pool 
# It have one thread safe task queue
# When the queue have the task the threads waked up 
# they execute the task and then go to sleep 


#Improvement 
#This solution does not ensure to clean all the remaing task in the job queue instead 
#it simply proceed to shutdown the job queue 
# Another issue with this solution is it does the busy waiting you can avoid the by using the 
# Condition variable 



import time, random
from threading import Thread, Condition, Semaphore, Event
from queue import Queue
import queue

class Job:
    def __init__(self, id, duration):
        self.id = id
        self.duration = duration

    def execute(self):
        time.sleep(self.duration)


class ThreadPool():
    # common queue which will hold the incoming jobs 
    taskQueue = Queue()
    # condition variable which will be used executor 
    # Not using this right now, using approach of busy waiting
    # However, it would be a better solution to use condition variable 
    # Basically you can model 
    #queueCondition = Condition() 

    # Special Thread which picks the next task from the
    # task queue instead of fixed target assigned at time 
    # of construction 
    class ExtendedPoolThread(Thread):
        def __init__(self, group = None, target = None, name = None, args = ..., kwargs = None, *, daemon = None):
            super().__init__(group, target, name, args, kwargs, daemon=daemon)
            self.shutdown_signal = Event()
            
        
        def run(self):
            print(f"Thread {self.name}: Started")
            while not self.shutdown_signal.is_set():
                try: 
                    task = ThreadPool.taskQueue.get(timeout=1)
                    print(f"Thread {self.name}: Starting Task {task.id}")
                    task.execute()
                except queue.Empty:
                    print(f"Thread {self.name}, Queue is empty at {time.strftime('%Y-%m-%d %H:%M:%S')}, moving to idle state")
                    pass
            print(f"Thread {self.name}, Finished")

        def shutdown(self):
            print(f"Thread {self.name}, Shutdown signal received")
            self.shutdown_signal.set()
        
                    

    def __init__(self, num):
        self.num = num
        self.threads = []

        for i in range(num):
            t = self.ExtendedPoolThread(name = f"W_{i}")
            self.threads.append(t) 
            t.start()


    def submit(self, job:Job):
        self.taskQueue.put(job)
        
    def size(self):
        self.taskQueue.qsize() 

    def shutdown(self):
        # mark shutdown event in each thread 
        for t in self.threads:
            t.shutdown()
            t.join()


# given a thread pool, following method 
# creates job at random interval and submit 
# that 
def periodic_job_creator(pool: ThreadPool):
    counter = 1
    for i in range(15):
        j = Job(f"J_{counter}",random.uniform(0.2,3))
        print(f"Submitting Job : Job({j.id}, {j.duration})")
        pool.submit(j)
        counter += 1 
        time.sleep(random.uniform(0.2,1))
    

if __name__ == "__main__":
    pool = ThreadPool(3)
    jc = Thread(target=periodic_job_creator, args=(pool,))
    # start job creation 
    jc.start()
    time.sleep(20)
    pool.shutdown()   
    jc.join()




