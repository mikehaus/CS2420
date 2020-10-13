"""
Main driver file for
P5 2420
Mike Hollingshaus
"""
from binarysearchtree import BinarySearchTree

########## ---------- BEGIN MAIN MODULE ---------- ##########

def main():
    """
    Main function. Creates BST, puts in preorder form
    prints list then goes through bst and prints all data.
    """
    bst = BinarySearchTree()
    for i in range(10):
        bst.add(i)
    inorder_bst = bst.inorder()
    bst.rebalance_tree()
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
