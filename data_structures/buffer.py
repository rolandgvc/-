class CircularBuffer:
    
    def __init__(self, size):
        self.buffer = [None]*size
        self.low = 0    # where to remove from
        self.high = 0   # where to add to
        self.size = size
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size
        
    def __len__(self):
        return self.count
        
    def add(self, value):
        if self.is_full():
            self.low = (self.low + 1) % self.size
        else:
            self.count += 1
        self.buffer[self.high] = value
        self.high = (self.high + 1) % self.size
    
    def remove(self):
        if self.count == 0:
          raise Exception ("Circular Buffer is empty")
        value = self.buffer[self.low]
        self.low = (self.low + 1) % self.size
        self.count -= 1
        return value
    
    def __iter__(self):
        idx = self.low
        num = self.count
        while num > 0:
            yield self.buffer[idx]
            idx = (idx + 1) % self.size
            num -= 1

    def __repr__(self):
        if self.is_empty():
          return '[]'
        return '[' + ','.join(map(str,self)) + ']'


