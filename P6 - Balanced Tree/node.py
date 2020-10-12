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
        self.data = data
        self.left_child = left
        self.right_child = right
        self.height = 0

    def is_leaf(self):
        """
        is_leaf returns true if it is a leaf node
        false if it is a parent node.
        """
        if self.left_child is None and self.right_child is None:
            return True
        return False

    def update_height(self):
        """
        update_height method used to update height
        of self.
        """
        if self.is_leaf():
            return 0
        elif self.left_child is None:
            self.height = 1 + self.right_child.height
        elif self.right_child is None:
            self.height = 1 + self.left_child.height
        else:
            self.height = 1 + max(self.left_child.height, self.right_child.height)

    def __str__(self):
        """
        Returns string representation of Node.
        """
        stringified_leaf_add = ''
        if self.is_leaf():
            self.height = 0
            stringified_leaf_add += ' [leaf]'
        stringified = str(self.data) + ' (' + str(self.height) + ')'
        stringified += stringified_leaf_add
        return stringified

########## ---------- END NODE CLASS DECLARATION ---------- ##########
