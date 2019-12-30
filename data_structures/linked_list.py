class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None

class LinkedList:
    def __init__(self, *start):
        self.head = None
        self.length = 0
        
        for _ in start:
            if self.head == None:
                self.head = Node(_)
            else:
                self.add_at_tail(_)

    def add_at_head(self, value):
        if self.head == None:
            self.head = Node(value)
        else: 
            temp = self.head
            self.head = Node(value)
            self.head.next = temp
        self.length += 1

    def add_at_tail(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(value)
        self.length += 1

    def delete_at_index(self, index):
        if self.head == None:
            raise Exception('List is empty.')
        
        if index == 0:
            if self.length > 1:
                self.head = self.head.next
            else:
                self.head = None

        temp = self.head
        i = 0
        while i < index-1 and temp.next != None:
            temp = temp.next
            i += 1
        
        if temp.next != None:
            temp.next = temp.next.next
        self.length -= 1
        
        return True
   
    def __iter__(self):
        temp = self.head
        while temp != None:
            yield temp.value
            temp = temp.next
        
    def __repr__(self):
        if self.head is None:
            return '[]'
        return '[{0:s}]'.format(','.join(map(str,self)))

    def __len__(self):
        return self.length

