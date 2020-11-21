from structures.stack import Stack


def postfix_to_infix(expression: str) -> str:
    operators = ['+', '-', '*', '/']
    result = ''
    tmp = Stack()

    comps = expression.split(' ')

    for component in comps:
        if component not in operators:
            tmp.push(component)
        else:
            right_operand = tmp.pop()
            left_operand = tmp.pop()

            tmp.push(f'({left_operand} {component} {right_operand})')

    for component in tmp:
        result += component

    return result


def infix_to_prefix(expression: str) -> str:
    operators = ['*', '/', '+', '-']
    result = ''
    tmp_op = Stack()

    comps = expression.split(' ')

    def has_higher_precedence(operator, compare):
        low_precedence = ['+', '-']
        high_precedence = ['*', '/']

        if operator in high_precedence and compare in low_precedence:
            return True
        elif operator in low_precedence and compare in high_precedence:
            return False

        return True

    for component in comps:
        if component.isalnum():
            result += f'{component} '

        elif component in operators:
            while not tmp_op.is_empty() and has_higher_precedence(tmp_op.peek(), component) and tmp_op.peek() != '(':
                result += f'{tmp_op.pop()} '
            tmp_op.push(component)

        elif component == '(':
            tmp_op.push(component)

        elif component == ')':
            while not tmp_op.is_empty() and tmp_op.peek() != '(':
                result += f'{tmp_op.pop()} '
            tmp_op.pop()

    while not tmp_op.is_empty():
        result += f'{tmp_op.pop()} '

    return result


def postfix_to_prefix(expression: str) -> str:
    pass


def eval_postfix(expression: str) -> str:
    operators = ['+', '-', '*', '/']
    tmp = Stack()

    def evaluate(left: str, op: str, right: str):
        left_comp = float(left)
        right_comp = float(right)

        if op == '+':
            return left_comp + right_comp
        elif op == '-':
            return left_comp - right_comp
        elif op == '*':
            return left_comp * right_comp
        else:
            return left_comp / right_comp

    comps = expression.split(' ')

    for component in comps:
        if component not in operators:
            tmp.push(component)
        else:
            right_operand = tmp.pop()
            left_operand = tmp.pop()

            tmp.push(f'{evaluate(left_operand, component, right_operand)}')

    return tmp.pop()
