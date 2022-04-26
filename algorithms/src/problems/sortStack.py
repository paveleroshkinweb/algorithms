def sortStack(stack):
	if len(stack) <= 1:
		return stack
	last_element = stack.pop()
	sortStack(stack)
	insertInPlace(stack, last_element)
	return stack


def insertInPlace(stack, element, next_to_insert=None):
	if len(stack) == 0 or stack[-1] < element:
		stack.append(element)
	else:
		last_element = stack.pop()
		insertInPlace(stack, element, last_element)
	if next_to_insert is not None:
		stack.append(next_to_insert)
