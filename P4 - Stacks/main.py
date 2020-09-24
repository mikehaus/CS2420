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

def determine_operator_priority(op1, op2):
    return priority[op1] >= priority[op2]

def process_line(stack, infix_string):
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
    infix_string = 'infix: '
    postfix_expression = 'postfix: '
    left_parenthesis_count = 0
    for char in expr:
        if char == '(':
            stack.push(Item(char))
            left_parenthesis_count += 1
            infix_string += char
        elif char.isnumeric():
            stack.push(Item(char))
            postfix_expression += char + ' '
            infix_string += char
            continue
        elif char == ' ':
            infix_string += char
            continue
        elif char == '\n':
            postfix_expression += last_operator
            process_line(stack, infix_string)
            continue
        elif (char == '+' or char == '-' or char == '*' or char == '/'):
            infix_string += char
            if last_operator == '':
                last_operator = char
                continue
            if (stack.size() > 0 and stack.top()._data != '(' and left_parenthesis_count <= 1):
                if last_operator != '':
                    if determine_operator_priority(char, last_operator):
                        postfix_expression += char + ' '
                        last_operator = ''
                    elif (not determine_operator_priority(char, last_operator) and left_parenthesis_count < 1):
                        postfix_expression += last_operator + ' '
                        last_operator = char
                    elif(not determine_operator_priority(char, last_operator) and left_parenthesis_count >= 1):
                        postfix_expression += last_operator + ' ' + char
                        last_operator = ''
                temp_op = stack.pop()
            stack.push(Item(char))
        else: 
            infix_string += char
            while stack.top()._data != '(':
                temp_op = stack.pop()
                if temp_op._data == '(':
                    left_parenthesis_count -= 1
                if last_operator != '':
                    postfix_expression += last_operator
                    last_operator = ''
    return postfix_expression

def parse_file(file):
    """
    Parse text of filepath file
    """
    infix_string = ''
    filelines = file.readlines()
    for line in filelines:
        in2post(line)
        char = file.read(1)

def main():
    data = open('data.txt', 'r')
    parse_file(data)
    return 

main()