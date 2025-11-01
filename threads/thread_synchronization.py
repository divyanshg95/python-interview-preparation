# Case 1 - Thread 3 starts two thread T1, T2, T3, All threds start doing their
#           own work, However, T3 must start a work once T1,T2 have reachers to
#           a certain point in the space then only T3 should make any further 
#           progress 


# you can implement following using barrir, join or semaphore 


import time
import random
from threading import Thread, Semaphore, Barrier

# Synchronisation using join
def task1(name):
    print(f"Thread {name} executing task")
    time.sleep(random.uniform(0.5,5))
    print(f"Thread {name} executing. task")


def task2(name):
    print(f"Thread {name} executing task")
    time.sleep(random.uniform(3,7))
    print(f"Thread {name} finishing task")

def task3(thread1, thread2, name):
    print(f"Thread {name} executing stage 1")
    time.sleep(random.uniform(3,7))
    print(f"Thread {name} finishing stage 1")
    
    thread1.join()
    thread2.join()
    
    print(f"Thread {name} executing stage 2")
    time.sleep(random.uniform(3,7))
    print(f"Thread {name} finishing stage 2")


def synchronisation_using_join():
    t1 = Thread(target=task1, args=("T1",))
    t2 = Thread(target=task2, args=("T2",))
    t3 = Thread(target=task3, args=(t1,t2,"T3",))
    t1.start()
    t2.start()
    t3.start()

    t3.join()




# following example show how the semaphore can be used for synchronisation work

def task_sema_1(semaphore:Semaphore, name):
    print(f"Thread {name} starting the task 1")
    time.sleep(random.uniform(3,5))
    print(f"Thread {name} finishing the task 1")
    semaphore.release()

def task_sema_2(semaphore:Semaphore, name):
    print(f"Thread {name} starting the task 2")
    time.sleep(random.uniform(3,5))
    print(f"Thread {name} finishing the task 2")
    semaphore.release()

def task_sema_3(sema1:Semaphore, sema2:Semaphore, name):
    print(f"Thread {name} starting the task 3 stage 1")
    time.sleep(random.uniform(0.2,0.5))
    print(f"Thread {name} finishing the task 3 state 1 ")
    
    sema1.acquire()
    sema2.acquire()

    print(f"Thread {name} starting the task 3 stage 2")
    time.sleep(random.uniform(3,5))
    print(f"Thread {name} finishing the task 3 stage 2 ")


def synchronisation_using_semaphore():
    s1 = Semaphore(0)
    s2 = Semaphore(0)

    t1 = Thread(target=task_sema_1, args=(s1,"T1",))
    t2 = Thread(target=task_sema_2, args=(s2,"T2",))
    t3 = Thread(target=task_sema_3, args=(s1, s2, "T3",))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()




if __name__ == "__main__":
    #synchronisation_using_join()
    synchronisation_using_semaphore()

    