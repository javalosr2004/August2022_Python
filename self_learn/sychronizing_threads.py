from concurrent.futures import thread
from re import X
import threading, time

x = 8192

'''using locks'''
def locks_threading():
    lock = threading.Lock() #locks a resource until it is done being used by current function
    #makes it basically synchronous

    def double():
        global x, lock
        lock.acquire()
        while x < 16384:
            x *=2
            print(x)
            time.sleep(1)
        print('Reached the maximum.')
        lock.release()

    def halve():
        global x, lock
        lock.acquire()
        while x > 1:
            x /= 2
            print(x)
            time.sleep(1)
        print('Reached the minimum.')
        lock.release()

    t1 = threading.Thread(target = halve)
    t2 = threading.Thread(target = double)

    t1.start()
    t2.start()

sempahore = threading.BoundedSemaphore(value = 5) #sets limit on how many threads can access a resource, 5 threads 
y = 1
def access(thread_number):
    global y
    print(f'Thread {thread_number} is trying to access value.')
    sempahore.acquire()
    print(f'Thread {thread_number} was granted access! ')
    time.sleep(10)
    print(f'Thread {thread_number} is now releasing value')
    sempahore.release()
    
for thread_number in range(1, 11):
    t = threading.Thread(target = access, args = (thread_number,)) # 1- 5 go first and are granted access and release it after 10 seconds, afterwards 6-10 follow up and gain access
    t.start()
    time.sleep(0.5)