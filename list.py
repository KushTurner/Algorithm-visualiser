import random

def makelst(num):
    lst = [*range(1, num+1)]
    random.shuffle(lst)
    return lst

arr = makelst(60)