"""
Implementation of Balanced BST for
CS2420 Project 6
Mike Hollingshaus
"""
from recursioncounter import RecursionCounter

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

########## ---------- END NODE CLASS DEFINITION ---------- ##########

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
        self._height = -1
        self.left_is_leaf = False

    def __len__(self):
        """
        Returns length of BST (How many Nodes)
        """
        _ = RecursionCounter()
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
        Does not add if duplicate cursor.
        """
        _ = RecursionCounter()
        if cursor is None:
            return Node(data)
        if cursor.data == data:
            return None
        if data < cursor.data:
            cursor.left_child = self.add_helper(cursor.left_child, data)
        if data > cursor.data:
            cursor.right_child = self.add_helper(cursor.right_child, data)
        cursor.update_height()
        return cursor

    def find(self, data):
        """
        Returns matched item.
        If item is not in tree, returns none.
        """
        if self.root.data == data:
            return self.root
        return self.find_helper(self.root, data)

    def find_helper(self, cursor, data):
        """
        Recursively searches through BST for
        matching data and returns data if found,
        If not found returns None.
        """
        _ = RecursionCounter()
        if cursor is None:
            return None
        if data < cursor.data:
            return self.find_helper(cursor.left_child, data)
        if data > cursor.data:
            return self.find_helper(cursor.right_child, data)
        return cursor

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
        _ = RecursionCounter()
        if cursor is None:
            return cursor
        if data < cursor.data:
            cursor.left_child = self.remove_helper(cursor.left_child, data)
            cursor.update_height()
        elif data > cursor.data:
            cursor.right_child = self.remove_helper(cursor.right_child, data)
            cursor.update_height()
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
            cursor.data = temp.data
            cursor.right_child = self.remove_helper(cursor.right_child, temp.data)
            cursor.update_height()
        return cursor

    def preorder(self):
        """
        Returns an iterator that performs a
        preorder traversal of the tree.
        """
        preorder_list = []
        if self.root is None:
            return preorder_list
        return self.preorder_helper(self.root, preorder_list)

    def preorder_helper(self, cursor, output):
        """
        Recursively iterates through tree via
        preorder traversal which is ROOT->LEFT->RIGHT
        """
        _ = RecursionCounter()
        if cursor is None:
            return
        if cursor is not None:
            output.append(cursor.data)
            self.preorder_helper(cursor.left_child, output)
            self.preorder_helper(cursor.right_child, output)
        return output

    def inorder(self):
        """
        Returns an iterator that performs an
        inorder traversal of the tree.
        """
        inorder_list = []
        if self.root is None:
            return inorder_list
        return self.inorder_helper(self.root, inorder_list)

    def inorder_helper(self, cursor, output):
        """
        Recursively iterates through tree via
        inorder traversal which is LEFT->ROOT->RIGHT
        """
        _ = RecursionCounter()
        if cursor is None:
            return
        if cursor is not None:
            self.inorder_helper(cursor.left_child, output)
            output.append(cursor.data)
            self.inorder_helper(cursor.right_child, output)
        return output

    def height(self):
        """
        Returns height of root node (height of tree).
        """
        if self.root is None:
            return -1
        return self._height

    def get_balance(self, cursor):
        """
        returns balance of tree for rebalancing.
        """
        h_left = 0
        h_right = 0
        if cursor is None:
            return 0
        if cursor.left_child is not None:
            h_left = cursor.left_child.height
        if cursor.right_child is not None:
            h_right = cursor.right_child.height
        return h_left - h_right

    def rotate_right(self, cursor):
        """
        Rotates over root.left
        """
        left = cursor.left_child
        left_right = left.right_child
        # Perform rotation 
        left.right_child = cursor
        cursor.left_child = left_right
        # Update heights 
        cursor.update_height()
        left_right.update_height() 
        # Return the new root 
        return left_right

    def rotate_left(self, cursor):
        """
        Rotates over root.right
        """
        right = cursor.right_child 
        right_left = right.left_child 
        # Perform rotation 
        right.left_child = cursor
        cursor.right_child = right_left
        # Update heights 
        cursor.update_height()
        right.update_height()
        # Return the new root 
        return right

    def rebalance_tree(self):
        """
        1) take middle value as root
        2) split list into left and right halves, excluding
        root.
        4) recursively rebuild the tree using steps 1 and 2 until done
        """
        if self.root is None:
            return None
        self.rebalance_helper(self.root)

    def rebalance_helper(self, cursor):
        """
        1) take middle value as root
        2) split list into left and right halves, excluding
        root.
        4) recursively rebuild the tree using steps 1 and 2 until done
        """
        _ = RecursionCounter()
        if cursor is None:
            return
        cursor.left_child = self.rebalance_helper(cursor.left_child)
        cursor.right_child = self.rebalance_helper(cursor.right_child)
        cursor = self.balance_node(cursor)
        return cursor

    def balance_node(self, cursor):
        #BALANCING ALGORITHM
        balance = self.get_balance(cursor)
        if balance < -1:
            if cursor.right_child.left_child is not None:
                cursor.right_child = self.rotate_right(cursor.right_child)
            cursor = self.rotate_left(cursor.right_child)
        if balance > 1:
            if cursor.left_child.right_child is not None:
                cursor.left_child = self.rotate_left(cursor.left_child)
            cursor = self.rotate_right(cursor.left_child)
        return cursor
        
    def __str__(self):
        """
        Returns a string representation of the BST.
        """
        output = ''
        if self.root is None:
            return output
        self.print_helper(self.root, self.height())
        return ''

    def print_helper(self, cursor, offset):
        """
        Recursive print helper for tree. Iterates
        retursively through tree and prints with spacing
        per offset.
        """
        _ = RecursionCounter()
        if cursor is None:
            return ''
        output = ''
        offset_counter = offset - self.root.height
        for i in range(offset_counter):
            output += '    '
        output += str(cursor)
        print(output)
        if cursor.left_child is None:
            if cursor.height > 0:
                output = ''
                offset_counter += 1
                for i in range(offset_counter):
                    output += '    '
                output += '[Empty]'
                print(output)
            elif self.left_is_leaf is True:
                output = ''
                for i in range(offset_counter):
                    output += '    '
                output += '[Empty]'
                print(output)
                self.left_is_leaf = False
        if cursor.left_child is not None:
            if cursor.left_child.is_leaf() and cursor.right_child is None:
                self.left_is_leaf = True
        self.print_helper(cursor.left_child, offset + 1)
        self.print_helper(cursor.right_child, offset + 1)

########## ---------- END BST CLASS DEFINITION ---------- ##########
