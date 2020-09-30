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

    def remove(self, data):
        """
        Removes data at Node with data.
        Void method.
        """
        if self.root.data() == data:
            return self.root.data()
        return self.remove_helper(self.root, data)

    def remove_helper(self, cursor, data):
        """
        Recursively does some stuff
        Implementing after inOrder.
        """
        return

    def preorder(self):
        """
        Returns an iterator that performs a
        preorder traversal of the tree.
        """
        perorder_list = []
        if self.root is None:
            return perorder_list
        return self.preorder_helper(self.root, perorder_list)

    def preorder_helper(self, cursor, output):
        """
        Recursively iterates through tree via
        preorder traversal which is ROOT->LEFT->RIGHT
        """
        output.append[cursor]
        if cursor is not None:
            return self.preorder_helper(cursor.left_child, output)
            return self.preorder_helper(cursor.right_child, output)
        return output

    def height(self):
        """
        Returns height of root node (height of tree).
        """
        if self.root is None:
            return None
        return self.root.height()

########## ---------- END BST CLASS DEFINITION ---------- ##########
