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

    def __len__(self):
        """
        Returns length of BST (How many Nodes)
        """
        out = self.preorder()
        return len(out)

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

    def smallest_child(self, child):
        curr = child
        while curr.left_child is not None:
            curr = curr.left_child
        return curr

    def remove(self, data):
        """
        Removes data at Node with data.
        Void method.
        """
        return self.remove_helper(self.root, data)

    def remove_helper(self, cursor, data):
        """
        Recursively does some stuff
        Implementing after inOrder.
        """
        if cursor is None:
            return cursor
        if data < cursor.data():
            cursor.left_child = self.remove_helper(cursor.left_child, data)
        elif data > cursor.data():
            cursor.right_child = self.remove_helper(cursor.right_child, data)
        else:
            if cursor.left_child is None:
                temp_node = cursor.right_child
                cursor = temp_node
                return temp_node
            elif cursor.right_child is None:
                temp_node = cursor.left_child
                cursor = temp_node
                return temp_node
            temp = self.smallest_child(cursor.right_child)
            cursor._data = temp.data()
            cursor.right_child = self.remove_helper(cursor.right_child, temp.data())
        return cursor

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
        if cursor is None:
            return
        if cursor is not None:
            cursor.update_height()
            output.append(cursor)
            self.preorder_helper(cursor.left_child, output)
            self.preorder_helper(cursor.right_child, output)
        return output

    def height(self):
        """
        Returns height of root node (height of tree).
        """
        if self.root is None:
            return 0
        return 1 + max(self.root.left_child.height(), self.root.right_child.height())

    def __str__(self):
        """
        Returns a string representation of the BST.
        """
        output = ''
        if self.root is None:
            return output
        return self.print_helper(self.root, )

    def print_helper(self, cursor, offset):
        """
        Recursive print helper for tree. Iterates
        retursively through tree and prints with spacing
        per offset.
        """
        return

########## ---------- END BST CLASS DEFINITION ---------- ##########
