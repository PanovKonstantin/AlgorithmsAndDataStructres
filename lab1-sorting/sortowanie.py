""" Implemintation of algorithms """


def bubble_sort(tab):
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(0, len(tab)-1):
            if tab[i] > tab[i+1]:   # if two nieghbor-elements are in the wrong order
                not_sorted = True
                tab[i], tab[i+1] = tab[i+1], tab[i]     # swap two nieghbor-elements in thier places
    return tab


def selection_sort(tab):
    for i in range(0, len(tab)-2):  # for every but last element of the list
        min = i
        for j in range(i+1, len(tab)):  # searching for a minimal unsorted element
            if tab[min] > tab[j]:
                min = j
        tab[i], tab[min] = tab[min], tab[i]     # swap i element with the minimal one
    return tab


def quick_sort(tab):

    def partition(tab, low, high):  # function, that arranges elements of given list from index "low" to "high" in two groups: "lesser" and "greater" than pivot(last element)
        i = low - 1     # index of the last element of the "less" group
        pivot = tab[high]   # set pivot as the last element
        for j in range(low, high):
            if tab[j] < pivot:
                i = i + 1
                tab[i], tab[j] = tab[j], tab[i]     # put element, that is less than pivot in a "less" group
        i = i + 1
        tab[high], tab[i] = tab[i], tab[high]   # put pivot between groups
        return tab, i   # return rearranged list and index of used pivot

    def quick(tab, low, high):  # controls quick sort recursion
        if low >= high:     # if given group is less than two elements, stop recursion
            return tab
        tab, pivot_index = partition(tab, low, high)    # rearrange given group
        tab = quick(tab, low, pivot_index-1)    # sort the "less" group
        tab = quick(tab, pivot_index+1, high)   # sort the "greater" group
        return tab

    tab = quick(tab, 0, len(tab)-1)
    return tab