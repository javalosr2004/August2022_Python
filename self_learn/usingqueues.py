import queue
import threading, time

counter = queue.Queue()

numbers = [num for num in range(10, 80, 10)]

for number in numbers:
    counter.put(number)

print('')

def print_num():
    global counter
    print('Getting counter number: ', end = '')
    try:
        print(counter.get_nowait())
    except:
        print('FAILED')
        


for i in range(10):
    t = threading.Thread(target = print_num)
    t.start()
    time.sleep(1)

print('')

