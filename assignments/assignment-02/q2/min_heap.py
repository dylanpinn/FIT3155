import math


class MinHeap:
    """Min heap using tuple items."""

    def __init__(self):
        self.length = 0
        self.items = []

    def insert(self, item):
        """Insert item into the min heap."""
        self.items.append(item)
        self.length += 1
        item_index = self.length - 1
        parent = self.__get_parent(item_index)
        while parent[1] > item[1] and not self.__is_root(item_index):
            parent_index = self.__parent(item_index)
            item_index = self.__swap(parent_index, item_index)
            parent = self.__get_parent(item_index)

    def min(self):
        """Return min item in heap."""
        return self.items[0]

    def pop_min(self):
        """Pop minimum item from the min heap."""
        if self.is_empty():
            return
        root = self.items[0]
        # Swap root and last item
        self.__swap(0, self.length - 1)
        # Remove last item
        self.items = self.items[:-1]
        self.length -= 1
        self.heapify(0)
        return root

    def is_empty(self):
        """Check if min heap is empty."""
        return self.length == 0

    def heapify(self, index):
        """Heapify the MinHeap."""
        smallest = index
        left = self.__left(index)
        right = self.__right(index)

        if left < self.length and self.items[left][1] < self.items[smallest][1]:
            smallest = left
        if right < self.length and self.items[right][1] < self.items[smallest][1]:
            smallest = right
        if smallest != index:
            self.__swap(smallest, index)
            self.heapify(smallest)

    def __swap(self, item_index, target_index):
        """Swap two items."""
        tmp = self.items[item_index]
        self.items[item_index] = self.items[target_index]
        self.items[target_index] = tmp
        return target_index

    def __get_parent(self, index):
        """Get parent item of the current index."""
        return self.items[self.__parent(index)]

    @staticmethod
    def __left(index):
        return 2 * index + 1

    @staticmethod
    def __right(index):
        return 2 * index + 2

    @staticmethod
    def __parent(index):
        """Get parent index of the current index."""
        return math.floor(index - 1 / 2)

    @staticmethod
    def __is_root(index):
        """Check if the current index is the root node."""
        return index == 0
