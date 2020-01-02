"""
Min/Max retrieval: O(1)
Add/Remove: O(log n)

"""

class Heap:
    def __init__(self, values=None):
        self.data = list(values) if values else []
        self.length = len(self.data)

        start = self.length//2 - 1
        for i in range(start, -1, -1):
            self._heapify(i)

    def is_empty(self):
        return self.length == 0

    def pop(self):
        if self.length == 0:
            raise ValueError("Heap is empty.")
        val = self.data[0]
        self.length -= 1
        self.data[0] = self.data[self.length]
        self._heapify(0)
        return val

    def add(self, value):
        # If I have the array full, extend it
        if self.length == len(self.data):
            self.data.append(value)
        else:
            # Add to list
            self.data[self.length] = value
        i = self.length
        self.length += 1

        # Restructure heap
        while i > 0:
            parent = (i-1) // 2
            if self.data[i] < self.data[parent]:
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else:
                break

    def _heapify(self, i):
        """Turn array into heap structure."""
        left = 2 * i + 1
        right = 2 * i + 2

        # Find smallest element of parent, left, right
        if left < self.length and self.data[left] < self.data[i]:
            smallest = left
        else:
            smallest = i

        if right < self.length and self.data[right] < self.data[smallest]:
            smallest = right

        # If smallest is not already the parent then swap and propagate
        if smallest != i:
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            self._heapify(smallest)

    def __len__(self):
        return self.length

    def __repr__(self):
        return '[' + ','.join(map(str, self.data[:self.length])) + ']'
