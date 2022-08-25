import threading, time


path = 'test.txt'
text = ''


'''You can edit the file during this process and it will output the newly saved file'''
def readFile():
    global path, text
    while True:
        with open(path, 'r') as f:
            text = f.read()
        time.sleep(3)

def printLoop():
    for x in range(10):
        print(text)
        time.sleep(1)
    
t1 = threading.Thread(target = readFile, daemon=True) #makes the thread into a daemon meaning, it can run in the background but it isn't required, it can be terminated with no issues to the main program
t2 = threading.Thread(target = printLoop) #once this printLoop ends, the daemon terminates as it is a background proccess rather than a main function

t1.start()
t2.start()