"""
Implementation of Stack for
CS2420 Project 4.
Mike Hollingshaus
"""

########## -- BEGIN ITEM CLASS DEFINITION -- ##########

class Item():
    """
    Class definition of Item (Node).
    """

    def __init__(self, data):
        """
        Item class constructor.
        """
        self._data = data
        self._next = None

    def data(self):
        """
        Return data at Item.
        """
        return self._data

    def next(self):
        """
        Return next item.
        """
        return self._next

########## -- END ITEM CLASS DEFINITION -- #########

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
        push_item = Item(item)
        if self._top is None:
            self._top = push_item
            self._size += 1
            return
        push_item._next = self._top
        self._top = push_item
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
        return current_top.data()

    def top(self):
        """
        Return the item on top of the stack without
        removing it. Raise an IndexError if the stack
        is Empty.
        """
        if self._top is None:
            raise IndexError('OUT OF BOUNDS: Stack is Empty')
        return self._top.data()

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
