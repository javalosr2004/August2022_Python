import threading, sys

event = threading.Event()

def myfunction():
    print('\nWaiting for event to trigger...')
    event.wait() #waits for event to trigger
    print('\nPerforming action XYZ now....')

t1 = threading.Thread(target=myfunction)
t1.start()

user_response = input('\nWould you like to trigger the event? (y/n)\n')
if user_response == 'y':
    event.set() #triggers the event
else:
    print('Event not set.')
    sys.exit()