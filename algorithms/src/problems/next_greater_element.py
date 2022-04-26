def nextGreaterElement(array):
    elements = [-1 for _ in range(len(array))]
    stack = []
    for i in range(2 * len(array)):
        index = i % len(array)

        while stack and array[stack[-1]] < array[index]:
            top = stack.pop()
            elements[top] = array[index]

        if elements[index] == -1:
            stack.append(index)

    return elements
