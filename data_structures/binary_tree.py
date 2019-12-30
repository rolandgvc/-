
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value <= self.value:
            self.left = self._add(self.left, value)
        else:
            self.right = self._add(self.right, value)

    def _add(self, parent, val):
        if parent is None:
            return Node(val)
        parent.add(val)
        return parent

    def remove(self, value):
        if value < self.value:
            self.left = self._remove(self.left, value)
        elif value > self.value:
            self.right = self._remove(self.right, value)
        else:
            if self.left is None:
                return self.right

            child = self.left
            while child.right:
                child = child.right
            
            value = child.value;
            self.left = self._remove(self.left, value)
            self.value = value
        
        return self

    def _remove(self, parent, value):
        if parent:
            return parent.remove(value)
        return None

    def __repr__(self):
        leftS = ''
        rightS = ''
        if self.left:
            leftS = str(self.left)
        if self.right:
            rightS = str(self.right)
        return "(L:" + leftS + " " + str(self.value) + " R:" + rightS + ")"

    def inorder(self):
        if self.left:
            for v in self.left.inorder():
                yield v

        yield self.value

        if self.right:
            for v in self.right.inorder():
                yield v

class BinaryTree:

    def __init__(self):
        self.root = None
   
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.add(value)

    def remove(self, val):
        if self.root:
            self.root = self.root.remove(val)

    def get_min(self):
        if self.root is None:
            raise ValueError("Binary Tree is empty")
        n = self.root
        while n.left != None:
            n = n.left
        return n.value

    def get_max(self):
        if self.root is None:
            raise ValueError("Binary Tree is empty")
        n = self.root
        while n.right != None:
            n = n.right
        return n.value
    
    def __contains__(self, target):
        """Check whether BST contains target value."""
        node = self.root
        while node:
            if target < node.value :
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return True
                
        return False

    def __iter__(self):
        """In order traversal."""
        if self.root:
            for e in self.root.inorder():
                yield e

    def __repr__(self):
        if self.root is None:
            return "()"
        return "str(self.root)

"""
Change Log:
-----------

"""
