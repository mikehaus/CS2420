"""
Main driver file for Stacks project
CS2420 P4
Mike Hollingshaus
"""
from stack import Stack
from item import Item

def main():
    stack = Stack()
    item = Item('{')
    stack.push(item)
    item = Item('1')
    stack.push(item)
    stack.pop()
    stack.pop()
    return 0

main()