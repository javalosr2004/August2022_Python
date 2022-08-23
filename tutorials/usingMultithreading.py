import threading, string

def function1():
    for x in range(10000):
        print('ONE')
    for x in range(10000):
        print('TWO')

function1()