import threading
x = 0
def increment():
    global x
    x+=1
def thread_task(lock):
    for k in range(100000):
        lock.acquire
        increment()
        lock.relase
def main_task():
    global x
    x=0
if __name__ == "__main__":
        
     lock = threading.Lock
t1=threading.Thread(target=thread_task,args=(lock))
t2=threading.Thread(target=thread_task,args=(lock))
t1.start()
t2.start()
t1.join()
t2.join()
for i in range(10):
        main_task()
        print("interation {0}:x={1}".format(i,x))
        
    


