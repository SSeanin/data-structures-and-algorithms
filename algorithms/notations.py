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
