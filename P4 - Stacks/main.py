"""
Main driver file for Stacks project
CS2420 P4
Mike Hollingshaus
"""
from stack import Stack
from item import Item

########## ---------- BEGIN MAIN FILE ---------- ##########

def determine_lesser_operator_priority(op1, top):
    """
    Function specifically to show priority of two
    operator arguments. Returns true if op1 is
    less than or equal to top.
    """
    operators = '+-/*'
    parenthesis = '()'
    priority = {
        '+': 0,
        '-': 0,
        '*': 1,
        '/': 1
    }

    try:
        op1prio = priority[op1]
        op2prio = priority[top]
        return bool(op1prio <= op2prio)
    except KeyError:
        return False

def check_valid_postfix_expr(expr):
    """
    Special counter to determine if string is
    a valid postfix expression or not. If char
    is literal increment, if char is operator
    decrement. If counter goes below 0, it's not
    valid.
    """
    counter = 0
    valid = True
    for char in expr:
        if char == ' ':
            continue
        if char.isnumeric():
            counter += 1
        elif ((char == '+') or (char == '-') or (char == '*') or (char == '/')):
            counter -= 1
        if counter < 0:
            valid = False
    return valid

def eval_postfix(expr):
    """
    Takes string postfix expression and evaluates
    then returns result as number. If expression is
    not valid, raise a SyntaxError.
    """
    if expr is None:
        raise ValueError('None is not a postfix expression')
    elif not check_valid_postfix_expr(expr):
        raise SyntaxError('Expression input is not a valid postfix expression')
    elif not isinstance(expr, str):
        raise ValueError("Expression input is not of type string")
    stack = Stack()
    for char in expr:
        if char == ' ':
            continue
        if char.isnumeric():
            stack.push(Item(char))
        else:
            if stack.size() == 1:
                raise SyntaxError("Not a valid postfix expression")
            operand_1 = float(stack.pop().data())
            operand_2 = float(stack.pop().data())
            if char == '+':
                stack.push(Item(operand_1 + operand_2))
            elif char == '-':
                stack.push(Item(operand_2 - operand_1))
            elif char == '*':
                stack.push(Item(operand_2 * operand_1))
            elif char == '/':
                stack.push(Item(operand_2 / operand_1))

    result = stack.pop().data()
    return result

def in2post(expr):
    """
    Takes infix expression as input and return a postfix
    expression as a string. If expression not valid, raise
    a SyntaxError. If parameter expr is not a string, raise
    a ValueError.
    """
    if not isinstance(expr, str):
        raise ValueError('Expression is not a string')
    stack = Stack()
    postfix_expression = ''
    left_paren_count = 0
    right_paren_count = 0
    for char in expr:
        if char == '(':
            left_paren_count += 1
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
            right_paren_count += 1
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
    if left_paren_count != right_paren_count:
        raise SyntaxError('Not a valid expression')
    while stack.size() > 0:
        popped = stack.pop().data()
        postfix_expression += ' ' + popped 
    print('postfix:' + postfix_expression)
    return postfix_expression

def parse_file(file):
    """
    Parse text of filepath file
    """
    infix_string = ''
    filelines = file.readlines()
    for line in filelines:
        infix_string = 'infix: ' + line
        if infix_string[len(infix_string) - 1] == '\n':
            infix_string = infix_string[:-1]
        print(infix_string)
        postfix_expr = in2post(line)
        answer = eval_postfix(postfix_expr)
        print('answer: ' + str(answer) + '\n')

def main():
    """
    Main Function. Opens file, reads it,
    then lets functions do the work.

    """
    data = open('data.txt', 'r')
    parse_file(data)
    data.close()

main()
########## ---------- END MAIN FILE ---------- ##########
