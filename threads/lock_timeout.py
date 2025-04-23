from threading import Lock, Thread 
from time import sleep 

# Demorate the use for timeout parameter in Lock.acquire 

lock = Lock()

def func1():
    try:
        print("Task 1, acquiring lock")
        lock.acquire(timeout=1)
        print("Task 1, lock is aquired, processing")
        sleep(5)
    finally:
        lock.release()

def func2():
        while True:
            print("Task 2, aquiring lock")
            if lock.acquire(timeout=1):
                try: 
                    print("Task 2, lock is aquired, processing")
                finally:
                    lock.release()
                    break
            else:
                print("Task 2, lock is aquire failed, doing another task")

if __name__ == "__main__":
     thread1 = Thread(target=func1)
     thread2 = Thread(target=func2)

     thread1.start()
     thread2.start()

     thread1.join()
     thread2.join()

     


    



