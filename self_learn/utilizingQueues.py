'''there are two different types of queues:
 LifoQueues which as the name implies means the last value entered into the queue is the first one out 
 and normal queues which follows the FiFo protocal.

 Collections: Dequeue
 Can do both

'''


import requests, threading
from bs4 import BeautifulSoup
from queue import Queue
from collections import deque

url_list = ['https://www.google.com', 'https://www.twitter.com', 'https://www.facebook.com', 'https://www.pvusd.net', 'https://www.youtube.com']

url_queue = Queue() #can not directly process a iterable
url_dequeue = deque() #can directly process a iterable

url_dequeue.extend(url_list)

for url in url_list:
    url_queue.put(url)

#dequeue using .pop method follows LiFo protocol .popleft follows FiFo

def requestUrl():
    global url_dequeue
    url = url_dequeue.popleft()

    '''
    print('GETTING STATUS CODE: ')
    print(url_html.status_code) #200 means OK
    '''

    url_html = requests.get(url).text

    getTitle(url_html)

def getTitle(url_html):
    soup = BeautifulSoup(url_html, 'lxml')
    try:
        print((soup.title.text).strip())
    except:
        print('NO TITLE')

for i in range(4):
    t = threading.Thread(target = requestUrl)
    t.start()
