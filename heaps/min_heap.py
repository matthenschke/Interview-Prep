# HEAP IMPLEMENTATION

'''
Left child is 2 * pos + 1
Right child is 2 * pos + 2
'''


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self.heapify(0)

    def remove(self):
        if len(self.heap) == 0:
            return
        self.heap[0] = self.heap.pop()
        self.heapify(0)

    def heapify(self, idx):
        l_child = 2 * idx + 1
        r_child = 2 * idx + 2
        min_idx = idx
        n = len(self.heap)

        if l_child < n and self.heap[l_child] < self.heap[min_idx]:
            min_idx = l_child

        if r_child < n and self.heap[r_child] < self.heap[min_idx]:
            min_idx = r_child

        if min_idx != idx:
            self.heap[idx], self.heap[min_idx] = self.heap[min_idx], self.heap[idx]
            self.heapify(min_idx)

    def print_heap(self):
        for item in self.heap:
            print(item)


if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.insert(5)
    min_heap.insert(2)
    min_heap.insert(1)
    min_heap.insert(10)
    min_heap.remove()

    min_heap.print_heap()
