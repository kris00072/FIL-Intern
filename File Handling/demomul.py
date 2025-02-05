from threading import *
import time
def f1():
    for i in range(1,11):
        time.sleep(1)
        print(2**i)

    print(time.time())    

print(time.time())
def f2():
    for i in range(1,11):
        time.sleep(1)
        print(i+i)
btime=time.time()        
f1()
f2()
print(time.time()-btime)        