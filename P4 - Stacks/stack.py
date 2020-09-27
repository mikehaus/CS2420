"""
Implementation of Stack for
CS2420 Project 4.
Mike Hollingshaus
"""
from item import Item

########## -- BEGIN STACK CLASS DEFINITION -- ##########

class Stack():
    """
    This Stack will be used specifically to
    translate and evaluate infix to postfix
    expressions.
    """
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, item):
        """
        Adds Item (node) to the top of stack.
        """
        if not isinstance(item, Item):
            item = Item(item)
        if self._top is None:
            self._top = item
            self._size += 1
            return
        item._next = self.top()
        self._top = item
        self._size += 1
        return

    def pop(self):
        """
        Remove top item from the stack without
        removing it. Raise IndexError if the
        stack is empty.
        """
        if self._top is None:
            raise IndexError('OUT OF BOUNDS: Stack is Empty')
        current_top = self._top
        self._top = self._top._next
        self._size -= 1
        return current_top

    def top(self):
        """
        Return the item on top of the stack without
        removing it. Raise an IndexError if the stack
        is Empty.
        """
        if self._top is None:
            raise IndexError('OUT OF BOUNDS: Stack is Empty')
        return self._top

    def size(self):
        """
        Return the number of items in the stack.
        """
        return self._size

    def clear(self):
        """
        Empty the Stack.
        """
        if self._size == 0:
            return
        for itr in range(0, self._size):
            self.pop()
        self._size = 0

########## -- END STACK CLASS DEFINITION -- ##########
