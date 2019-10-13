class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'(value={self.value}, ' \
               f'left={None if not self.left else self.left.value}, ' \
               f'right={None if not self.right else self.right.value})'
