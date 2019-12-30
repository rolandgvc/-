"""

Implementeation of a queue using linked lists. In real life however, a deque
shall be used for faster performance.

"""

from .linkedlist import Node

class Queue:
    def __init__(self, *start):
        self.head = None
        self.tail = None
        for _ in start:
            self.append(_)

    def append(self, value):
        """Add value to end of queue."""
        new_node = Node(value, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def is_empty(self):
        return self.head == None

    def pop(self):
        """Remove first value from queue."""
        if self.head is None:
            raise Exception ("Queue is empty.")
        val = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return val

    def __iter__(self):
        """Iterator of values in queue."""
        n = self.head
        while n != None:
            yield n.value
            n = n.next
        
    def __repr__(self):
        """String representation of queue."""
        if self.head is None:
            return 'queue:[]'

        return 'queue:[{0:s}]'.format(','.join(map(str,self)))

    def __len__(self):
        """Count values in queue."""
        n = self.head
        count = 0
        while n != None:
            count += 1
            n = n.next
        return count

