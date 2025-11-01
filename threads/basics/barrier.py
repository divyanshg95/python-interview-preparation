from  threading import Thread, Barrier
import time
import random 

# In this example the task is divided in two stages. Three thread 
# execute same task, They all finished first stage then proceed for the 
# second stage 

def runner(barrier: Barrier, name):
    print(f"Thead: {name} executing stage 1")
    time.sleep(random.uniform(0.5, 5))
    print(f"Thread: {name}: Finished the stage 1")
    barrier.wait()

    print(f"Thread: {name} started executing stage 2")
    time.sleep(random.uniform(0.5, 5))
    print(f"Thread: {name} Finished stage 2")


if __name__ == "__main__":
    barrier = Barrier(3)
    
    t1 = Thread(target= runner, args=(barrier, "T1",))
    t2 = Thread(target= runner, args=(barrier, "T2",))
    t3 = Thread(target= runner, args=(barrier, "T3",))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()




