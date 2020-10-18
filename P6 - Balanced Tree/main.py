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
    for i in range(11):
        bst.add(i)
    bst.rebalance_tree()
    preorder = bst.preorder()
    output = ''
    for node_data in preorder:
        output += str(node_data)
        output += ', '
    print(output)
    str(bst)
    removevals = [21, 9, 4, 18, 15, 7]
    for remove in removevals:
        bst.remove(remove)
    str(bst)

main()
