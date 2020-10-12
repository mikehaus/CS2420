"""
Main driver file for
P5 2420
Mike Hollingshaus
"""
from balancedBST import BinarySearchTree

########## ---------- BEGIN MAIN MODULE ---------- ##########

def main():
    """
    Main function. Creates BST, puts in preorder form
    prints list then goes through bst and prints all data.
    """
    bst = BinarySearchTree()
    addvals = [21, 26, 30, 9, 4, 14, 28, 18, 15, 10, 2, 3, 7]
    for add in addvals:
        bst.add(add)
    inorder_bst = bst.inorder()
    output = ''
    for node_data in inorder_bst:
        output += str(node_data)
        output += ', '
    print(output)
    str(bst)
    removevals = [21, 9, 4, 18, 15, 7]
    for remove in removevals:
        bst.remove(remove)
    str(bst)

main()
