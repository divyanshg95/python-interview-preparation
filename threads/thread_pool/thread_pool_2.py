#Design 
# This is another implementation of the thread pool.
# Compared to thread_pool_1.py implementation, here 
# we have two major changes 
# 1. We are using condition variable to avoid the busy waiting 
# 2. We are not extending the actual thread class instead we 
#    we are using standard thread class
# 3. It contains the Singleton Class for the ThreadPool 

# Note: I have made it overly complex, for interview you simply need to have 
# a queue and a considiton variable busy waiting is also fine 



# My code was not working AI made following changes and improved it 
# Progress update — what I changed and verified

# What I found: The original hang happened because threads were created with target=self.executeTasks() (calling the method immediately). That made the main thread run the worker loop and block on the condition wait, so worker threads never started.
# Changes made (in thread_pool_2.py):
# Start threads with target=self.executeTasks (no parentheses) and daemon=True.
# Rewrote executeTasks so workers wait on the condition correctly, fetch tasks without holding the lock, execute tasks, and exit when shutdown is set.
# Fixed submit to put the job while holding the condition and call notify() while holding it.
# Implemented shutdown to set the shutdown event, notify_all() to wake waiters, and join worker threads.
# Added task_done() and made size() return the queue size.
# Verification: I ran the script. Worker threads W_0..W_2 started properly, processed submitted jobs, and the process shut down cleanly at the end. Output shows jobs being started and threads finishing.

# Following are small improvements suggested by the AI 
# Possible follow-ups / small improvements

# Use per-instance queue and condition instead of class-level shared ones if you intend multiple independent ThreadPool instances.
# Add exception handling around task execution to avoid a crashing task killing a worker.
# Add unit tests: a simple test that submits N quick tasks and asserts they all complete (use queue.join()).
# Consider exposing a blocking shutdown(timeout) to avoid indefinite join waits.


import time, random
from threading import Thread, Condition, Event
from queue import Queue
import queue
import threading

class Job:
    def __init__(self, id, duration):
        self.id = id
        self.duration = duration

    def execute(self):
        time.sleep(self.duration)


class ThreadPool():  
    _instance = None
    _task_queue = Queue()
    _queue_condition = Condition()     

    def __new__(cls, *args, **kargs):
        if cls._instance is None: 
            cls._instance = super().__new__(cls)
        
        return cls._instance
    
    def __init__(self, num):
        print("Requesting to Create Thread Pool Class")
        if not hasattr(self, 'instanciated'):
            self.instanciated = True
            self.num = num
            self.threads = []
            self.shutdown_signal = Event()
            
            for i in range(num):
                # pass the callable, don't call it here
                t = Thread(target=self.executeTasks, name=f"W_{i}")
                self.threads.append(t) 
                t.start()
    
    def executeTasks(self):
        name = threading.current_thread().name
        print(f"Thread {name}: Started")
        while not self.shutdown_signal.is_set():
            task = None
            with ThreadPool._queue_condition:
                # wait until a task is available or shutdown is requested
                while ThreadPool._task_queue.empty() and not self.shutdown_signal.is_set():
                    print(f"Thread {name}, Queue is empty at {time.strftime('%Y-%m-%d %H:%M:%S')}, moving to idle state")
                    ThreadPool._queue_condition.wait(timeout=1)

                if self.shutdown_signal.is_set():
                    break

                try:
                    task = ThreadPool._task_queue.get_nowait()
                except queue.Empty:
                    # loop back and wait again
                    continue

            # execute the task outside the condition lock 
            # to avoid 
            if task:
                print(f"Thread {name}: Starting Task {task.id}")
                try:
                    task.execute()
                finally:
                    try:
                        ThreadPool._task_queue.task_done()
                    except Exception:
                        pass

        print(f"Thread {name}, Finished")

    def shutdown(self):
        print("Shutdown signal received")
        # signal threads to stop
        self.shutdown_signal.set()
        # wake up all waiting workers so they can exit
        with ThreadPool._queue_condition:
            ThreadPool._queue_condition.notify_all()

        # join worker threads
        for t in self.threads:
            t.join()


    def submit(self, job: Job):
        with ThreadPool._queue_condition:
            ThreadPool._task_queue.put(job)
            # notify a waiting worker
            ThreadPool._queue_condition.notify()

    def size(self):
        return ThreadPool._task_queue.qsize()



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
    pool1 = ThreadPool(3)

    print(f"Both Thread Pool are same {pool} {pool1}")

    jc = Thread(target=periodic_job_creator, args=(pool,))
    # start job creation 
    jc.start()
    time.sleep(20)
    pool.shutdown()   
    jc.join()

# Why are you executing task outside the condition lock

# Short answer: to avoid holding the condition lock while running potentially long or blocking work — that prevents starving other worker threads and avoids needless contention or deadlocks. Here’s why and what to watch for.

# Why we pop the task while holding the lock, then execute it after releasing:

# Correctness of queue access: we remove the task from the shared queue while holding the condition so two workers can’t take the same task. That gives a short critical section for queue bookkeeping and preserves the intended semantics.
# Minimize lock hold time: task.execute() can sleep, do I/O, or call other code. If the lock stayed held during execution, no other worker could access the queue or be notified — throughput falls dramatically.
# Avoid deadlocks and missed wakeups: long-running work inside the lock delays notify/notify_all usage and can produce hard-to-debug timing issues.
# Why this is safe here:

# Python’s Queue is already thread-safe, so the queue operations themselves are safe. We use the Condition as the wait/notify mechanism (to avoid busy-waiting). Taking a task under the condition and then releasing it before executing preserves both correctness and responsiveness.
# We call task_done() after execution (outside the condition) which is fine — it only updates queue internals and is thread-safe.
# When you might want to hold the lock during execution

# If the task body must run while some shared invariants (protected by the same lock) are held, then you must keep the lock for the duration of that critical section. But prefer narrowing that protected portion inside task.execute() (or have the task acquire the specific lock it needs), rather than blocking the global queue condition.
# If tasks need to interact with the thread pool internals atomically (rare), design specific synchronization primitives for that need.
# Alternatives and trade-offs

# Use queue.get(block=True) with optional timeout and avoid a separate Condition entirely. Simpler, but you lose the fine-grained control over wakeups/notify semantics if you needed them.
# Use per-pool (instance) Condition and queue rather than class-level shared ones if you want independent pools.
# If tasks must perform short critical updates to shared state, let them acquire a dedicated lock inside their execute() rather than holding the queue condition.
# Edge cases to watch for

# If task.execute() raises an exception, ensure the worker catches it so the thread doesn’t die silently. (Wrap execute() with try/except.)
# If tasks call back into pool.submit() or other pool methods that rely on the same Condition, ensure those methods are safe to be called from worker threads (notify must be done while holding the Condition).
# If you rely on queue.join() to wait for all tasks to finish, ensure task_done() is always called even when execute() errors (use finally).
# If you want, I can:

# Add try/except/finally around task execution to ensure task_done() always gets called.
# Replace the Condition+manual wait with a simpler queue.get(timeout=...) loop to simplify the code.
# Convert class-level queue/condition to instance-level so multiple pools are independent.