"""

Simple implementation of a linked list.

"""

class Node:
    def __init__(self, value, tail = None):
        """Node in a Linked List."""
        self.value = value
        self.next  = tail

class LinkedList:
    def __init__(self, *start):
        self.head = None
        for _ in start:
            self.prepend(_)

    def prepend(self, value):
        """Add value at beginning of the list."""
        self.head = Node(value, self.head)

    def pop(self):
        """Remove first value."""
        if self.head is None:
            raise Exception ("Linked list is empty.")
        val = self.head.value
        self.head = self.head.next
        return val

    def remove(self, value):
        """Remove value from list."""
        n = self.head
        last = None
        while n != None:
            if n.value == value:
                if last == None:
                    self.head = self.head.next
                else:
                    last.next = n.next
                return True
            n = n.next
        return False
        
    def __iter__(self):
        n = self.head
        while n != None:
            yield n.value
            n = n.next
        
    def __repr__(self):
        if self.head is None:
            return 'link:[]'
        return 'link:[{0:s}]'.format(','.join(map(str,self)))

    def __len__(self):
        n = self.head
        count = 0
        while n != None:
            count += 1
            n = n.next
        return count

