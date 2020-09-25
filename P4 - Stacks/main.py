"""
Main driver file for Stacks project
CS2420 P4
Mike Hollingshaus
"""
import sys
import re
from stack import Stack
from item import Item

operators = '+-/*'
parenthesis = '()'
priority = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1
}

def determine_greater_operator_priority(op1, top):
    try:
        op1prio = priority[op1]
        op2prio = priority[top]
        if op1prio <= op2prio:
            return True
        else:
            return False
    except KeyError:
        return False

    return priority[op1] >= priority[op2]

def process_line(stack):
    #if stack.size() != 0:
        #stack.clear()
    return

def in2post(expr):
    """
    Takes infix expression as input and return a postfix
    expression as a string. If expression not valid, raise
    a SyntaxError. If parameter expr is not a string, raise
    a ValueError.
    """
    stack = Stack()
    last_operator = ''
    postfix_expression = ''
    for char in expr:
        if char == '(':
            stack.push(Item(char))
        elif char.isnumeric():
            postfix_expression += ' ' + char
            continue
        elif char == ' ':
            continue
        elif char == '\n':
            while stack.size() > 0:
                popped = stack.pop()._data
                postfix_expression += ' ' + popped
            continue
        elif char == ')':
            while (stack.size() != 0 and char != '('):
                char = stack.pop()._data
                if char == '(':
                    break
                postfix_expression += ' ' + char
            if (stack.size() > 0 and char != '('):
                return postfix_expression
        else:
            while (stack.size() != 0 and determine_greater_operator_priority(char, stack.top()._data)):
                popped = stack.pop()._data
                if popped == '(':
                    break
                postfix_expression += ' ' + popped
            stack.push(Item(char))
    print('postfix:' + postfix_expression + '\n')
    return postfix_expression

def parse_file(file):
    """
    Parse text of filepath file
    """
    infix_string = ''
    filelines = file.readlines()
    for line in filelines:
        infix_string = 'infix: ' + line
        infix_string = infix_string[:-1]
        print(infix_string)
        in2post(line)
        char = file.read(1)

def main():
    data = open('data.txt', 'r')
    parse_file(data)
    return 

main()