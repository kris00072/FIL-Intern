import time
from threading import *
l=Lock()
def wish(name):
    l.acquire()
    for i in range(5):
        print("Good Morning",end="")
        time.sleep(2)
        print(name)
    l.release()
t1=Thread(target=wish,args=("rahul",)) 
t2=Thread(target=wish,args=("Steve",)) 
t1.start()
t2.start()      