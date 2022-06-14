def generate_brackets(length):
    brackets = []

    def helper(open_used, closed_used, substr=''):
        if open_used == closed_used == length:
            brackets.append(substr)
        elif open_used == length:
            helper(open_used, closed_used + 1, substr + ')')
        elif open_used == closed_used:
            helper(open_used + 1, closed_used, substr + '(')
        else:
            helper(open_used + 1, closed_used, substr + '(')
            helper(open_used, closed_used + 1, substr + ')')

    helper(1, 0, '(')

    return brackets
