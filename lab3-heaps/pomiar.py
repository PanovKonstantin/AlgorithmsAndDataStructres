import timeit

from Heap import Heap

import numpy as np


def heap_2():
    heap = Heap(array=array, child_number=2)


def heap_3():
    heap = Heap(array=array, child_number=3)


def heap_4():
    heap = Heap(array=array, child_number=4)


array = []
print('{:>22s}'.format("2-ary"), end="")
print('{:>23s}'.format("3-ary"), end="")
print('{:>24s}'.format("4-ary"))
for i in range(0, 10):
    for element in np.random.randint(low=1, high=3000, size=1000):
        array.append(element)
    print('{:>14s}'.format(f"{i+1}000 elements:"), end="")
    print("\t", '{:<20s}'.format(str(timeit.timeit(heap_2, number=100)/100)), end="\t")
    print('{:<20s}'.format(str(timeit.timeit(heap_3, number=100)/100)), end="\t")
    print('{:<20s}'.format(str(timeit.timeit(heap_4, number=100)/100)))
