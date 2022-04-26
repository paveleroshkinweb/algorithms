class MinMaxStack:

    def __init__(self):
        self.stack = []


    def peek(self):
        if self.stack:
            return self.stack[-1]['value']

    
    def pop(self):
        if self.stack:
            node = self.stack.pop()
            return node['value']


    def push(self, number):
        node = {
            'value': number,
            'min': min(number, self.stack[-1]['min']) if self.stack else number,
            'max': max(number, self.stack[-1]['max']) if self.stack else number
        }
        self.stack.append(node)


    def getMin(self):
        if self.stack:
            return self.stack[-1]['min']


    def getMax(self):
        if self.stack:
            return self.stack[-1]['max']