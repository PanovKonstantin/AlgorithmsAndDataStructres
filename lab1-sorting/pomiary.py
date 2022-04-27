""" Implemintation of measurements """

import re
import timeit


bubble_sort_setup = """
import sys
def bubble_sort(tab):
    no_swap=False
    while not no_swap:
        no_swap = True
        for i in range(0, len(tab)-1):
            if tab[i] > tab[i+1]:
                no_swap = False
                helpVar = tab[i+1]
                tab[i+1] = tab[i]
                tab[i] = helpVar
    return tab
sys.setrecursionlimit(10**7)"""

selection_sort_setup = """import sys
def selection_sort(tab):
    for i in range(0, len(tab)-2):
        min = i
        for j in range(i+1, len(tab)):
            if tab[min] > tab[j]:
                min = j
        tab[i], tab[min] = tab[min], tab[i]
    return tab
sys.setrecursionlimit(10**7)"""

quick_sort_setup = """import sys
def quick_sort(tab):

    def partition(tab, low, high):
        i = low - 1
        pivot = tab[high]
        for j in range(low, high):
            if tab[j] < pivot:
                i = i + 1
                tab[i], tab[j] = tab[j], tab[i]
        i = i + 1
        tab[high], tab[i] = tab[i], tab[high]
        return tab, i

    def quick(tab, low, high):
        if low >= high:
            return tab
        tab, pivot_index = partition(tab, low, high)
        tab = quick(tab, low, pivot_index-1)
        tab = quick(tab, pivot_index+1, high)
        return tab

    tab = quick(tab, 0, len(tab)-1)
    return tab
sys.setrecursionlimit(10**7)"""

file = open("pan-tadeusz.txt", encoding="utf-8")
text = file.read()
text = re.split(' |\n|\n ', text)   # split text by white spaces and new lines
text = [word for word in text if word != '' and word != '-']    # delete empty spaces and dashes
with open("results.txt", "w") as f:
    result = "\t\tbubble sort;\tselection sort;\tquick sort;\n"
    for n in [2000, 3000, 4000, 5000]:
        result += f"{n} elements:\t"
        result += str(round(timeit.timeit(f"bubble_sort({text[0:n]})", setup=bubble_sort_setup, number=1), 7))
        result += ';\t'
        result += str(round(timeit.timeit(f"selection_sort({text[0:n]})", setup=selection_sort_setup, number=1), 7))
        result += ';\t'
        result += str(round(timeit.timeit(f"quick_sort({text[0:n]})", setup=quick_sort_setup, number=1), 7))
        result += ';\n'
    print(result)
    f.write(result)
