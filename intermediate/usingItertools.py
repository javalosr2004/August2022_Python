from itertools import *

def usingProduct():
    a = [1, 2]
    b = [3]

    prod = product(a, b, repeat=2) #will execute the product of both iterations
    print(prod) #becomes an iterater
    prod = list(prod)
    print(prod)

usingProduct()