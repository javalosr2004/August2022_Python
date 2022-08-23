#collections: Counter | namedtuple | OrderedDict | defaultdict | deque

from collections import *
from typing import DefaultDict

def using_counter():
    a = 'aaaaaaaaabbbbcccc'
    my_counter = Counter(a) #lists the count of each 'key', 9 a's, 4 b's, and 4 c's

    print(my_counter.most_common(3)[0][0]) #lists the most common items, the integer is the amount listed, this will print the absolute most common item

def using_namedTuple():
    Point = namedtuple('Point', 'x,y, z') #creates a class named Point
    pt = Point(1, -7, 3)

    print(pt.x, pt.y, pt.z)


def using_OrderedDict():
    #remembers the order that items are stored, not primarily useful after python 3.7
    ordered_dict = OrderedDict()
    ordered_dict['a'] = 1
    ordered_dict['b'] = 2
    ordered_dict['c'] = 3

    print(ordered_dict.items())

def using_defaultDict():
    #only difference is that it will have a default value if a key has not been set

    d = DefaultDict(int) #sets the default type to an integer
    d['a'] = 1
    d['b'] = 2

    #if a key does not exist it will return a default value of an integer, which will be zero
    print(d['c'])

def using_deque():
    #can be used to add or remove elements from both ends of a list
    d = deque()

    d.append(1)
    d.append(2)

    print(d)

    d.appendleft(0)

    print(d)

    print(d.pop()) #returns and removes element from the right
    print(d)

    print(d.popleft())
    print(d)

    d.extend([2, 3, 4]) #adds elements from an iteration to the right side
    d.extendleft([-1, 0]) #appends elements from an iteration to the left side

    print(d)
    d.rotate(1) #moves elements one time to the right
    print(d)
    d.rotate(-1) #moves elements one time to the left
    print(d)

using_deque()