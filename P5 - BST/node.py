"""
Node class for CS 2420
Project 5 BST
Mike Hollingshaus
"""

########## ---------- BEGIN NODE CLASS DEFINITION ----------- ##########

class Node():
    """
    Basic implementation of a Node in Python.
    """
    def __init__(self, data, left=None, right=None):
        """
        Constructor method. Node has the following
        attributes:
        data: int
        left_child: Node
        right_child: Node
        height: int
        """
        self._data = data
        self.left_child = left
        self.right_child = right
        self._height = 0

    def is_leaf(self):
        """
        is_leaf returns true if it is a leaf node
        false if it is a parent node.
        """
        if self.left_child is None and self.right_child is None:
            return False
        return True

    def update_height(self, height):
        """
        update_height method used to update height
        of self.
        """
        self._height = height

    def __str__(self):
        """
        Returns string representation of Node.
        """
        stringified = str(self._data) + ' (' + str(self._height) + ')'
        return stringified

    def data(self):
        """
        Getter method for Node data.
        Returns data in Node.
        """
        return self._data

########## ---------- END NODE CLASS DECLARATION ---------- ##########
