# This implementation of reader_writer prefers write operation 
# if any write operation is in waiting then it will block further readers 
# to enter the system 


#idea : their are writer which are waiting for the resouce lock, then don't 
#       allow reader to enter in the system 

from threading import Thread, Semaphore, Lock , Condition
import time 
import random


read_count = 0 
write_count = 0
read_count_lock = Lock()
write_count_lock = Condition()
resource_lock = Lock() # exclusive lock used to protect the writer 

def read(name):
    global write_count
    global read_count
    print(f"Thread {name} : wants to read")
    with write_count_lock:
        while write_count != 0:
            print(f"Thread {name} : Writers are waiting, going to sleep")
            write_count_lock.wait()
        
        with read_count_lock: 
            if read_count == 0:
                resource_lock.acquire()
            read_count += 1

    print_status(name)    
    print(f"Thread {name} reading the data")
    time.sleep(random.uniform(0.2,3))


    with read_count_lock:
        if read_count == 1:
            resource_lock.release()
        read_count -= 1

    print(f"Thread {name} finished reading the data")




def print_status(name):
    with read_count_lock:
        with write_count_lock:
            print(f"CONCURRENT READERS: {read_count}")
            print(f"CONCURRENT WRITER: {write_count}")


def write(name):
    global write_count
    print(f"Thread {name} : wants to write")
    with write_count_lock:
        write_count += 1
    print_status(name)
    with resource_lock: 
        print(f"Thread {name} : writing")
        time.sleep(random.uniform(0.2,1))
    with write_count_lock:
        write_count -= 1
        if write_count == 0:
            write_count_lock.notify_all()
    print(f"Thread {name} : Finished writing")






# generate readers
def gen_readers():
    readers = []
    for i in range(5):
        r = Thread(target=read, args=(f"R_{i}",))
        readers.append(r)
        r.start()
        time.sleep(random.uniform(0.2, 3))
    
    for r in readers:
        r.join()

def gen_writers():
    writers = []
    for i in range(5):
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


