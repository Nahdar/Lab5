

class Heap:
    def __init__(self):
        self.heap_array = []

    def insert(self, k):
        self.heap_array.append(k)

        i = len(self.heap_array) - 1

        while self.smaller_than_parent(i):
            self.heap_array[i], self.heap_array[int(1/2)] = self.heap_array[int(1/2)], self.heap_array[i]
            i = int(i/2)

    def extract_min(self):
        if self.is_empty():
            return None
        i = len(self.heap_array)
        min_elem = self.heap_array[0]

        self.heap_array[0], self.heap_array[i - 1] = self.heap_array[i - 1], self.heap_array[0]

        self.heap_array.pop(i - 1)

        while not self.is_valid():
            for i in range(1, len(self.heap_array)):
                if self.heap_array[i] < self.heap_array[int(i / 2)]:
                    self.heap_array[i], self.heap_array[int(i/2)] = self.heap_array[int(i/2)], self.heap_array[i]

        return min_elem

    def is_empty(self):
        return len(self.heap_array) == 0

    def smaller_than_parent(self, i):
        return self.heap_array[i] > self.heap_array[int(i/2)]

    def is_valid(self):
        for i in range(1, len(self.heap_array)):
            if self.heap_array[i] < self.heap_array[int(i/2)]:
                return False

        return True

    def get_smallest(self):

        if self.heap_array is None or len(self.heap_array) < 1:
            return -1

        return self.heap_array[0]

    def get_max_sibling_gap(self):

        max_sib_gp = -1
        i = 0
        while (2 * i) + 2 < len(self.heap_array):
            left_sib = (2 * i) + 1
            right_sib = (2 * i) + 2

            sib_gp = self.heap_array[right_sib] - self.heap_array[left_sib]

            if sib_gp > max_sib_gp:
                max_sib_gp = sib_gp

            i += 1

        return max_sib_gp
