# if using mutex the spin lock is required in case of the producer
# consumer because once the thread goes to sleep their is now once which 
# informs it about the state change of the shared data. 
# if we use the condition variable which internally is combination of 
# lock and notify method. 
# If we use the condition variable then thread can go to sleep using the wait 
# method and can be again notified using the condition variable. You can think 
# condition variable as a a lock which also notifies the waiting threads in case 
# of the state change in the shared data protected under it


from collections import deque
from threading import Thread, Condition
import time 
import random
import counter


class ProcBuffer: 
    b = deque(maxlen=5)
    condition = Condition()


def producer(thread_id):
    print(f"Producer {thread_id}: Started")
    for i in range(10):
        with ProcBuffer.condition:
            while len(ProcBuffer.b) == ProcBuffer.b.maxlen:
                print(f"Producer {thread_id}: buffer is full, sleeping..")
                ProcBuffer.condition.wait()

            c = counter.Counter.getNext()
            item = f"item_{c}"
            print(f"Producer {thread_id}: generating {item}")
            ProcBuffer.b.append(item)
            ProcBuffer.condition.notify()
    time.sleep(0.5)


def consumer(thread_id):
    print(f"Consumer {thread_id}: Started")
    while True: 
        with ProcBuffer.condition:
            while not ProcBuffer.b:
                print(f"Consumer {thread_id}: Buffer is empty")
                ProcBuffer.condition.wait()
            
            item = ProcBuffer.b.popleft()
            print(f"Consumer {thread_id}: read item {item}")
            ProcBuffer.condition.notify()
        time.sleep(0.2)

if __name__ == "__main__":

    producers = []
    consumers = []

    for i in range(3):
        producers.append(Thread(target= producer, args =(i,)))
        consumers.append(Thread(target= consumer, args= (i,)))

    for i in range(3): 
        producers[i].start()
        consumers[i].start()

    for p in producers:
        p.join()
    for c in consumers:
        c.join()


