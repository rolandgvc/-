"""
    Implementation of a prefix tree of all lowercase words using
    linked lists.

"""

def traverse(node, prefix):
    """Generate all words recursively."""
    if node.word:
        yield prefix

    for c in 'abcdefghijklmnopqrstuvwxyz':
        next_c = ord(c) - ord('a')
        if node.next[next_c]:
            for _ in traverse(node.next[next_c], prefix + c):
                yield _

class PrefixNode:
    def __init__(self, suffix):
        self.next  = [None]*26
        self.word = False
        
        if len(suffix) == 0:
            self.word = True
            return

        idx = ord(suffix[0]) - ord('a')
        if self.next[idx] is None:
            self.next[idx] = PrefixNode(suffix[1:])
        else:
            self.next[idx].add(suffix[1:])
            

    def add(self, suffix):
        """Add rest of suffix."""
        if suffix == '':
            if self.word:
                return False
            self.word = True
            return True
        else:
            idx = ord(suffix[0]) - ord('a')
            if self.next[idx] is None:
                self.next[idx] = PrefixNode(suffix[1:])
                return True
            else:
                return self.next[idx].add(suffix[1:])

    def remove(self, suffix):
        """Remove rest of suffix."""
        if suffix == '':
            if self.word:
                self.word = False
                return True
            return False
        else:
            idx = ord(suffix[0]) - ord('a')
            if self.next[idx] is None:
                return False
            else:
                return self.next[idx].remove(suffix[1:])

    def __repr__(self):
        """Representation for debugging."""
        num = 0
        for n in self.next:
            if n:
                num += 1
        return 'pn:' + str(num) + "@" + str(self.word)
    
class PrefixTreeLinkedList:
    def __init__(self, *start):
        """Demonstrate prefix tree in Python give strings."""
        self.head  = [None]*26
        for _ in start:
            self.add(_.lower())

    def add(self, value):
        """Add value to prefix tree."""
        idx = ord(value[0]) - ord('a')
        if self.head[idx] is None:
            self.head[idx] = PrefixNode(value[1:])
            return True
        else:
            return self.head[idx].add(value[1:])

    def remove(self, value):
        """Remove value from prefix tree."""
        idx = ord(value[0]) - ord('a')
        if self.head[idx] is None:
            return False
        else:
            return self.head[idx].remove(value[1:])

    def __contains__(self, value):
        """Determine if value is contained in the prefix tree."""
        idx = ord(value[0]) - ord('a')
        value = value[1:]
        n = self.head[idx]
        while n != None:
            if len(value) == 0:
                return n.word
            idx = ord(value[0]) - ord('a')
            value = value[1:]
            n = n.next[idx]
            
        return False

    def __iter__(self):
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            idx = ord(ch) - ord('a')
            if self.head[idx]:
                for _ in traverse(self.head[idx], ch):
                    yield _
        
    def __repr__(self):
        if self.head is None:
            return 'prefixLL:[]'
        return 'prefixLL:[{0:s}]'.format(','.join(map(str,self)))

    def __len__(self):
        count = 0
        for _ in self:
            count += 1
        return count
    
