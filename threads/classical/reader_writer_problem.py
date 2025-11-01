# Following solution provide a reader preferred solution which might lead 
# to write startvation 


from threading import Semaphore, Lock,Thread
import time
import random

read_count = 0      # variable denotes the number of the readers
read_count_Lock = Lock()  # lock protect the concurrent access of the read_count variable 
w_lock = Lock()     # exclusive projects the resource 



def read(name):
    global read_count
    print(f"Thred {name} : trying to read the data")
    with read_count_Lock:
        if read_count == 0:
            w_lock.acquire(blocking = True)
        read_count += 1
        print(f"NUMBER OF CONCURRENT {read_count}")
    
    
    print(f"Thread {name} reading the data")
    time.sleep(random.uniform(0.4,1))

    with read_count_Lock:
        read_count -= 1
        if read_count == 0:
            w_lock.release()
        print(f"Thread {name}: Finished reading :{read_count}")
    
    
def write(name): 
    print(f"Thread {name}: Trying to write data")
    with w_lock:
        print(f"Thread {name}: writing data")
        time.sleep(random.uniform(2,5))
    print(f"Thread {name}: Finished Writing ")


# generate readers
def gen_readers():
    readers = []
    for i in range(20):
        r = Thread(target=read, args=(f"R_{i}",))
        readers.append(r)
        r.start()
        time.sleep(random.uniform(0.2, 3))
    
    for r in readers:
        r.join()

def gen_writers():
    writers = []
    for i in range(20):
        w = Thread(target=write, args=(f"W_{i}",))
        writers.append(w)
        w.start()
        time.sleep(random.uniform(0.1,2))
    for w in writers:
        w.join()



if __name__ == "__main__":
    gen_w = Thread(target=gen_writers)
    gen_r = Thread(target=gen_readers)

    gen_w.start()
    gen_r.start()

    gen_w.join()
    gen_r.join()







        

