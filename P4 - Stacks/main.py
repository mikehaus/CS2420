"""
Main driver file for Stacks project
CS2420 P4
Mike Hollingshaus
"""
from stack import Stack
from item import Item

########## ---------- BEGIN MAIN FILE ---------- ##########

OPERATORS = '+-/*'
PARENTHESIS = '()'
PRIORITY = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1
}

def determine_lesser_operator_priority(op1, top):
    """
    Function specifically to show priority of two
    operator arguments. Returns true if op1 is
    less than or equal to top.
    """
    try:
        op1prio = PRIORITY[op1]
        op2prio = PRIORITY[top]
        return bool(op1prio <= op2prio)
    except KeyError:
        return False

def eval_postfix(expr):
    """
    Takes string postfix expression and evaluates
    then returns result as number. If expression is
    not valid, raise a SyntaxError.
    """
    return expr

def in2post(expr):
    """
    Takes infix expression as input and return a postfix
    expression as a string. If expression not valid, raise
    a SyntaxError. If parameter expr is not a string, raise
    a ValueError.
    """
    stack = Stack()
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
                popped = stack.pop().data()
                postfix_expression += ' ' + popped
            continue
        elif char == ')':
            while (stack.size() != 0 and char != '('):
                char = stack.pop().data()
                if char == '(':
                    break
                postfix_expression += ' ' + char
            if (stack.size() > 0 and char != '('):
                return postfix_expression
        else:
            while (stack.size() != 0 and determine_lesser_operator_priority(
                                                                        char,
                                                                        stack.top().data())):
                popped = stack.pop().data()
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

def main():
    """
    Main Function. Opens file, reads it,
    then lets functions do the work.
    """
    data = open('data.txt', 'r')
    parse_file(data)

main()

########## ---------- END MAIN FILE ---------- ##########
