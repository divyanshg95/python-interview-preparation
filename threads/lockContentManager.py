from threading import Thread, Lock 
from time import sleep 

lock = Lock()

def func1() -> None:
    print("Thread 1 acquiring lock")
    with lock:
        print("Thread 1 acquired lock")
        sleep(3)
    print("Thread 1 released lock")

def func2() -> None:
    print("Thread 2 acquiring lock")
    with lock:
        print("Thread 2 acquired lock")
        sleep(1)
    print("Thread 2 released lock")


if __name__ == "__main__":
    thread1 = Thread(target=func1)
    thread2 = Thread(target=func2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    


