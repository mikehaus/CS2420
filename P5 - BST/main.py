"""
Main driver file for
P5 2420
Mike Hollingshaus
"""
from binarysearchtree import BinarySearchTree
from node import Node

########## ---------- BEGIN MAIN MODULE ---------- ##########

def main():
    bst = BinarySearchTree()
    addvals = [21, 26, 30, 9, 4, 14, 28, 18, 15, 10, 2, 3, 7]
    for add in addvals:
        bst.add(add)
    fulloutput = bst.__str__()
    print(fulloutput)
    removevals = [21, 9, 4, 18, 15, 7]
    for remove in removevals:
        bst.remove(remove)
    partialoutput = bst.preorder()
    for val in partialoutput:
        print(str(val))
    bst.__str__()

main()
