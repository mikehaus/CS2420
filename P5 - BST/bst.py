"""
Implementation of BinarySearchTree ADT for
CS2420 Project 5
Mike Hollingshaus
"""
from node import Node

########## ---------- BEGIN BST CLASS DEFINITION ---------- ##########

class BinarySearchTree():
    """
    Basic Implementation of BinarySearchTree ADT.
    Contains methods:
    is_empty
    __len__
    height
    __str__
    add
    remove
    find
    inorder
    height
    """
    def __init__(self):
        """
        BST constructor method.
        """
        self.root = None

    def is_empty(self):
        """
        Boolean function returns True if empty,
        False if not.
        """
        if self.root is None:
            return True
        return False

    def add(self, data):
        """
        If empty adds node as root.
        If not adds recursively.
        """
        if self.is_empty():
            self.root = Node(data)
            return
        return self.add_helper(self.root, data)

    def add_helper(self, cursor, data):
        """
        Adds node recursively through tree.
        """
        if cursor is None:
            return Node(data)
        if data < cursor.data():
            cursor.left_child = self.add_helper(cursor.left_child, data)
        if data > cursor.data():
            cursor.right_child = self.add_helper(cursor.right_child, data)
        return cursor

    def find(self, data):
        """
        Returns matched item.
        If item is not in tree, returns none.
        """
        if self.root.data() == data:
            return data
        return self.find_helper(self.root, data)

    def find_helper(self, cursor, data):
        """
        Recursively searches through BST for
        matching data and returns data if found,
        If not found returns None.
        """
        if cursor is None:
            return None
        if data < cursor.data():
            return self.find_helper(cursor.left_child, data)
        if data > cursor.data():
            return self.find_helper(cursor.right_child, data)
        return cursor.data()

########## ---------- END BST CLASS DEFINITION ---------- ##########
