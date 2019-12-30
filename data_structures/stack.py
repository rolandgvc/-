"""
    Simple implementation of a stack with lists.
    
"""

class Stack:

  def __init__(self):
    self.stack = []

  def is_empty(self):
    return len(self.stack) == 0

  def push(self, x):
    self.stack.append(x)

  def pop(self):
    if self.is_empty():
      raise Exception('Stack is empty.')
    return self.stack.pop()

  def __repr__(self):
    return 'stack:' + str(self.stack)