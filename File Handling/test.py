from threading import Thread
import time

def f1():
    start_time = time.time()
    for i in range(1, 11):
        time.sleep(1)
        print(f"f1: {2**i}")
    end_time = time.time()
    return end_time - start_time  

def f2():
    start_time = time.time()
    for i in range(1, 11):
        time.sleep(1)
        print(f"f2: {i + i}")
    end_time = time.time()
    return end_time - start_time  

execution_time_f1 = None
execution_time_f2 = None

def wrapper_f1():
    global execution_time_f1
    execution_time_f1 = f1() 

def wrapper_f2():
    global execution_time_f2
    execution_time_f2 = f2()  

t1 = Thread(target=wrapper_f1)
t2 = Thread(target=wrapper_f2)


t1.start()
t2.start()


t1.join()
t2.join()


print(f"Execution time of f1: {execution_time_f1:.2f} seconds")
print(f"Execution time of f2: {execution_time_f2:.2f} seconds")
