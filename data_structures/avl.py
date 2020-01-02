class Node:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def compute_height(self):
        """Compute height of node in BST."""
        height = -1
        if (self.left):
            height = max(height, self.left.height)
        if (self.right):
            height = max(height, self.right.height)

        self.height = height + 1

    def height_difference(self):
        """Compute height difference of node's children in BST."""
        leftTarget = 0
        rightTarget = 0
        if (self.left):
            leftTarget = 1 + self.left.height
        if (self.right):
            rightTarget = 1 + self.right.height

        return leftTarget - rightTarget

    def recursive_height(self):
        """Compute height of node in BST recursively."""
        height = -1
        if (self.left):
            height = max(height, self.left.recursive_height())
        if (self.right):
            height = max(height, self.right.recursive_height())

        return height + 1

    def recursive_height_difference(self):
        """Compute height difference of node's children in BST recursively."""
        leftTarget = 0
        rightTarget = 0
        if (self.left):
            leftTarget = 1 + self.left.recursive_height()
        if (self.right):
            rightTarget = 1 + self.right.recursive_height()

        return leftTarget - rightTarget

    def assert_AVL(self):
        """Validate AVL property for BST node."""
        if abs(self.recursive_height_difference()) > 1:
            return False
        if (self.left):
            if not self.left.assert_AVL():
                return False
        if (self.right):
            if not self.right.assert_AVL():
                return False

        return True

    def rotate_right(self):
        """Perform right rotation around given node."""
        newRoot = self.left
        grandson = newRoot.right
        self.left = grandson
        newRoot.right = self

        self.compute_height()
        return newRoot

    def rotate_left(self):
        """Perform left rotation around given node."""
        newRoot = self.right
        grandson = newRoot.left
        self.right = grandson
        newRoot.left = self

        self.compute_height()
        return newRoot

    def rotate_left_right(self):
        """Perform left, then right rotation around given node."""
        child = self.left
        newRoot = child.right
        grand1 = newRoot.left
        grand2 = newRoot.right
        child.right = grand1
        self.left = grand2

        newRoot.left = child
        newRoot.right = self

        child.compute_height()
        self.compute_height()
        return newRoot

    def rotate_right_left(self):
        """Perform right, then left rotation around given node."""
        child = self.right
        newRoot = child.left
        grand1 = newRoot.left
        grand2 = newRoot.right
        child.left = grand2
        self.right = grand1

        newRoot.left = self
        newRoot.right = child

        child.compute_height()
        self.compute_height()
        return newRoot

    def add(self, val):
        newRoot = self

        if val <= self.value:
            self.left = self._add(self.left, val)
            if self.height_difference() == 2:
                if val <= self.left.value:
                    newRoot = self.rotate_right()
                else:
                    newRoot = self.rotate_left_right()
        else:
            self.right = self._add(self.right, val)
            if self.height_difference() == -2:
                if val > self.right.value:
                    newRoot = self.rotate_left()
                else:
                    newRoot = self.rotate_right_left()

        newRoot.compute_height()
        return newRoot

    def _add(self, parent, val):
        if parent is None:
            return Node(val)

        parent = parent.add(val)
        return parent

    def remove(self, val):
        newRoot = self
        if self.value == val:
            if self.left is None:
                return self.right

            child = self.left
            while child.right:
                child = child.right

            key = child.value
            self.left = self._remove(self.left, key)
            self.value = key

            if self.height_difference() == -2:
                if self.right.heightDifference() <= 0:
                    newRoot = self.rotate_left()
                else:
                    newRoot = self.rotate_right_left()
        elif self.value > val:
            self.left = self._remove(self.left, val)
            if self.height_difference() == -2:
                if self.right.heightDifference() <= 0:
                    newRoot = self.rotate_left()
                else:
                    newRoot = self.rotate_right_left()
        else:
            self.right = self._remove(self.right, val)
            if self.height_difference() == 2:
                if self.left.heightDifference() >= 0:
                    newRoot = self.rotate_right()
                else:
                    newRoot = self.rotate_left_right()

        newRoot.compute_height()
        return newRoot

    def _remove(self, parent, val):
        if parent:
            return parent.remove(val)
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
        """In order traversal."""
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

    def __str__(self):
        if self.root:
            return str(self.root)

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = self.root.add(value)

    def __contains__(self, target):
        node = self.root
        while node:
            if node.value == target:
                return True
            elif node.value > target:
                node = node.left
            else:
                node = node.right

        return False

    def remove(self, val):
        if self.root:
            self.root = self.root.remove(val)

    def __iter__(self):
        if self.root:
            for e in self.root.inorder():
                yield e

    def assert_AVL(self):
        if self.root:
            return self.root.assert_AVL()
        return True

    def __repr__(self):
        if self.root is None:
            return "()"
        return str(self.root)
