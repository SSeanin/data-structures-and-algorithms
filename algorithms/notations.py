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
