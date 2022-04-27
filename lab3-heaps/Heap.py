
import numpy as np


class Heap:
    def __init__(self, array=[], child_number=2):
        self.array = []
        self.len = -1
        self.child_number = child_number  # 3 for 3-ary, 4 for 4-ary and so on.
        for element in array:
            self.insert(element)

    def parent(self, index):
        return int((index-1)/self.child_number)

    def swap(self, i_1, i_2):
        self.array[i_1], self.array[i_2] = self.array[i_2], self.array[i_1]

    def insert(self, value):
        self.array.append(value)
        index = self.len + 1
        parent_index = self.parent(index)
        while self.array[index] > self.array[parent_index]:
            self.swap(index, parent_index)
            if parent_index == 0:  # break, if at root
                break
            index = parent_index
            parent_index = self.parent(index)
        self.len += 1

    def show(self):
        max_level = 0
        level_counter = 0
        while self.len > level_counter:
            max_level += 1
            level_counter += self.child_number**max_level
        level = 0
        level_counter = 0
        group = 0
        for i in range(0, len(self.array)):
            if i > level_counter:
                print()
                level += 1
                level_counter += self.child_number**level
                group = 0
            group += 1
            if group == self.child_number:
                print(self.array[i], "| ", end='')
                group = 0
            else:
                print(self.array[i], " ", end='')


heap = Heap(array=np.random.randint(low=1, high=100, size=50), child_number=4)
heap.show()
