# HEAP IMPLEMENTATION

'''
Left child is 2 * pos + 1
Right child is 2 * pos + 2
'''


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        cur_idx = len(self.heap) - 1
        self.heapify_up(cur_idx)

    def remove(self):
        if len(self.heap) == 0:
            return
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

    def heapify_up(self, idx):
        parent_idx = (idx - 1) // 2
        while parent_idx >= 0 and self.heap[parent_idx] < self.heap[idx]:
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def heapify_down(self, idx):
        l_child = 2 * idx + 1
        r_child = 2 * idx + 2
        max_idx = idx
        n = len(self.heap)

        if l_child < n and self.heap[l_child] > self.heap[max_idx]:
            max_idx = l_child

        if r_child < n and self.heap[r_child] > self.heap[max_idx]:
            max_idx = r_child

        if max_idx != idx:
            self.heap[idx], self.heap[max_idx] = self.heap[max_idx], self.heap[idx]
            self.heapify_down(max_idx)

    def print_heap(self):
        for item in self.heap:
            print(item)


if __name__ == "__main__":
    min_heap = MaxHeap()
    min_heap.insert(5)
    min_heap.insert(2)
    min_heap.insert(1)
    min_heap.insert(10)

    min_heap.remove()
    min_heap.print_heap()
