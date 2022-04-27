import timeit
import numpy as np


data = np.random.randint(low=1, high=3000, size=10000)

BST_setup = """class BST:
    def __init__(self, array):
        self.main_node = BSTnode(array[0])
        for element in array[1:]:
            self.main_node.insert(element)

    def insert(self, value):
        self.main_node.insert(value)

    def delete(self, value):
        self.main_node.delete(value)


class BSTnode:
    def __init__(self, value):
        self.value = value
        self.duplicates_counter = 0
        self.left_node = None
        self.right_node = None

    def is_leaf(self):
        if self.right_node is None and self.left_node is None:
            return True
        return False

    def is_only_left_child(self):
        if self.left_node is not None and self.right_node is None:
            return True
        return False

    def is_only_right_child(self):
        if self.left_node is None and self.right_node is not None:
            return True
        return False

    def insert(self, value):
        if value == self.value:
            self.duplicates_counter += 1
        elif(value > self.value):
            if self.right_node is None:
                self.right_node = BSTnode(value)
            else:
                self.right_node.insert(value)
        else:
            if self.left_node is None:
                self.left_node = BSTnode(value)
            else:
                self.left_node.insert(value)

    def most_left(self):
        if self.left_node is not None:
            return self.left_node.most_left()
        temp = self.value, self.duplicates_counter
        return temp

    def delete(self, value):
        if value < self.value:
            self.left_node = self.left_node.delete(value)
            return self
        elif value > self.value:
            self.right_node = self.right_node.delete(value)
            return self
        if self.is_leaf():
            if self.duplicates_counter == 0:
                return None
            self.duplicates_counter -= 1
            return self
        elif self.is_only_left_child():
            if self.duplicates_counter == 0:
                return self.left_node
            self.duplicates_counter -= 1
            return self
        elif self.is_only_right_child():
            if self.duplicates_counter == 0:
                return self.right_node
            self.duplicates_counter -= 1
            return self
        if self.duplicates_counter == 0:
            value, counter = self.right_node.most_left()
            self.right_node = self.right_node.delete(value)
            self.value = value
            self.duplicates_counter = counter
            return self
        self.duplicates_counter -= 1
        return self

    def find(self, value):
        if value == self.value:
            return self
        elif value > self.value:
            return self.right_node.find(value)
        else:
            return self.left_node.find(value)


class AVL:
    def __init__(self, array):
        self.main_node = AVLnode(array[0])
        for element in array[1:]:
            self.main_node = self.main_node.insert(element)

    def delete(self, value):
        self.main_node = self.main_node.delete(value)
sys.setrecursionlimit(10**7)
"""

AVL_setup = """class AVL:
    def __init__(self, array):
        self.main_node = AVLnode(array[0])
        for element in array[1:]:
            self.main_node = self.main_node.insert(element)

    def delete(self, value):
        self.main_node = self.main_node.delete(value)


class AVLnode:
    def __init__(self, value):
        self.value = value
        self.duplicates_counter = 0
        self.left_node = None
        self.right_node = None
        self.height = 0

    def insert(self, value):
        if self.value == value:
            self.duplicates_counter += 1
        elif value > self.value:
            # right child
            if self.right_node is None:
                self.right_node = AVLnode(value)
                if self.left_node is None:
                    self.height += 1
            else:
                self.right_node = self.right_node.insert(value)
                if self.right_node.height == self.height:
                    self.height += 1
        else:
            # left child
            if self.left_node is None:
                self.left_node = AVLnode(value)
                if self.right_node is None:
                    self.height += 1
            else:
                self.left_node = self.left_node.insert(value)
                if self.left_node.height == self.height:
                    self.height += 1
        self = self.balance()
        return self

    def delete(self, value):
        if value < self.value:
            self.left_node = self.left_node.delete(value)
        elif value > self.value:
            self.right_node = self.right_node.delete(value)
        elif value == self.value:
            if self.duplicates_counter != 0:
                self.duplicates_counter -= 1
                return self
            else:
                if self.left_node is None and self.right_node is None:
                    return None
                elif self.left_node is None:
                    self = self.right_node
                elif self.right_node is None:
                    self = self.left_node
                else:
                    temp = self.right_node.most_left()
                    self.duplicates_counter = temp.duplicates_counter
                    self.value = temp.value
                    self.right_node = self.right_node.delete(temp.value)
        self = self.calculateHeight()
        if self.height >= 2:
            self = self.balance()
            self = self.calculateHeight()
        return self

    def balance(self):
        if self.left_node is None and self.right_node is None:
            return self
        elif self.left_node is None:
            if self.right_node.height >= 2:
                return self.leftRotation()
            return self
        elif self.right_node is None:
            if self.left_node.height >= 2:
                return self.rightRotation()
            return self
        elif self.left_node.height - self.right_node.height == 2:
            if self.left_node.right_node is None:
                return self.rightRotation()
            if self.left_node.left_node is None:
                self.left_node = self.left_node.leftRotation()
                return self.rightRotation()
            if self.left_node.right_node.height <= self.left_node.left_node.height:
                return self.rightRotation()
            if self.left_node.right_node.height > self.left_node.left_node.height:
                self.left_node = self.left_node.leftRotation()
                return self.rightRotation()
        elif self.right_node.height - self.left_node.height == 2:
            if self.right_node.left_node is None:
                return self.leftRotation()
            if self.right_node.right_node is None:
                self.right_node = self.right_node.rightRotation()
                return self.leftRotation()
            if self.right_node.left_node.height <= self.right_node.right_node.height:
                return self.rightRotation()
            if self.right_node.left_node.height > self.right_node.right_node.height:
                self.right_node = self.right_node.rightRotation()
                return self.leftRotation()
        return self

    def calculateHeight(self):
        if self.right_node is None and self.left_node is None:
            self.height = 0
        elif self.right_node is None:
            self.height = self.left_node.height + 1
        elif self.left_node is None:
            self.height = self.right_node.height + 1
        else:
            self.height = max(self.left_node.height, self.right_node.height) + 1
        return self

    def rightRotation(self):
        new = self.left_node.calculateHeight()
        self.left_node = new.right_node
        new.right_node = self.calculateHeight()
        return new

    def leftRotation(self):
        new = self.right_node.calculateHeight()
        self.right_node = new.left_node
        new.left_node = self.calculateHeight()
        return new

    def most_left(self):
        if self.left_node is not None:
            return self.left_node.most_left()
        return self
    sys.setrecursionlimit(10**7)"""

BST_setup += f"\ndata = []"
AVL_setup += f"\ndata = []"
for element in data:
    BST_setup += f"\ndata.append({element})"
    AVL_setup += f"\ndata.append({element})"

print("\nCzas stworzenia BST:")
for i in range(1000, 10001, 1000):
    print(f"Dla {i} elementów: ")
    print(timeit.timeit(f"test = BST(data[:{i}])", setup=BST_setup, number=1))

print("\nCzas stworzenia AVL:")
for i in range(1000, 10001, 1000):
    print(f"Dla {i} elementów: ")
    print(timeit.timeit(f"test = AVL(data[:{i}])", setup=AVL_setup, number=1))

BST_setup += "\ntest = BST(data[:2000])"
print("\nCzas usuwania w BST z 2000 elementów:")
for i in range(100, 1001, 100):
    BST_setup += f"\ndeleteData = []"
    for j in range(i-100, i):
        BST_setup += f"\ndeleteData.append({data[j]})"
    print(f"Dla {i} elementów: ")
    print(timeit.timeit(f"[test.delete(element) for element in deleteData]", setup=BST_setup, number=1))

AVL_setup += "\ntest = AVL(data[:2000])"
print("\nCzas usuwania w AVL z 2000 elementów:")
for i in range(100, 1001, 100):
    AVL_setup += f"\ndeleteData = []"
    for j in range(i-100, i):
        AVL_setup += f"\ndeleteData.append({data[j]})"
    print(f"Dla {i} elementów: ")
    print(timeit.timeit(f"[test.delete(element) for element in deleteData]", setup=AVL_setup, number=1))