SKIP_SIGN = ' '
OPEN_BRACKET = '('
CLOSE_BRACKET = ')'

PLUS = '+'
MINUS = '-'
MULTIPLY = '*'
DIVIDE = '/'
POWER = '^'
REMAINDER = '%'

OPERATIONS = {
    PLUS: lambda a, b: a + b,
    MINUS: lambda a, b: a - b,
    MULTIPLY: lambda a, b: a * b,
    DIVIDE: lambda a, b: a / b,
    POWER: lambda a, b: a ^ b,
    REMAINDER: lambda a, b: a % b
}

HIGH_ORDER = {MULTIPLY, DIVIDE, POWER, REMAINDER}

ERROR_MESSAGE = "Invalid string provided!"


def evaluate(expression):
    stack = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char == SKIP_SIGN:
            i += 1
            continue
        if char in OPERATIONS:
            if not stack or stack[-1] in OPERATIONS:
                raise ValueError(ERROR_MESSAGE)
            stack.append(char)
            i += 1
        else:
            if char.isnumeric():
                number = ''
                while i < len(expression) and expression[i].isnumeric():
                    number += expression[i]
                    i += 1
                if len(number) > 1 and number[0] == '0':
                    raise ValueError(ERROR_MESSAGE)
                int_value = int(number)
            else:
                raise ValueError(ERROR_MESSAGE)
            if stack and stack[-1] not in OPERATIONS:
                raise ValueError(ERROR_MESSAGE)
            if not stack:
                stack.append(int_value)
            else:
                if stack[-1] in HIGH_ORDER:
                    operation = stack.pop()
                    operand = stack.pop()
                    handler = OPERATIONS[operation]
                    stack.append(handler(operand, int_value))
                else:
                    stack.append(int_value)
    if not stack:
        return None
    if len(stack) % 2 == 0:
        raise ValueError(ERROR_MESSAGE)
    while len(stack) > 1:
        right = stack.pop()
        handler = OPERATIONS[stack.pop()]
        left = stack.pop()
        stack.append(handler(left, right))
    return stack[0]

