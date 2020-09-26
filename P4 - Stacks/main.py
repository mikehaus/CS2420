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

def eval_postfix(expr):
    """
    Takes string postfix expression and evaluates
    then returns result as number. If expression is
    not valid, raise a SyntaxError.
    """
    stack = Stack()
    for char in expr:

        if char == ' ':
            continue

        if char.isnumeric():
            stack.push(Item(char))

        else:
            if stack.size() == 1:
                raise SyntaxError("Not a valid postfix expression")
            operand_1 = stack.pop().data()
            operand_2 = stack.pop().data()
            stack.push(Item(str(float(eval(operand_2 + char + operand_1)))))

    result = str(stack.pop().data())
    return result

def in2post(expr):
    """
    Takes infix expression as input and return a postfix
    expression as a string. If expression not valid, raise
    a SyntaxError. If parameter expr is not a string, raise
    a ValueError.
    """
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
        raise ValueError('Not a valid expression')
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
        infix_string = infix_string[:-1]
        print(infix_string)
        postfix_expr = in2post(line)
        answer = eval_postfix(postfix_expr)
        print('answer: ' + answer)

def main():
    """
    Main Function. Opens file, reads it,
    then lets functions do the work.
    """
    data = open('data.txt', 'r')
    parse_file(data)

main()

########## ---------- END MAIN FILE ---------- ##########
