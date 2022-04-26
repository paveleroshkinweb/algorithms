def moveElementToEnd(array, toMove):
	pointer1 = len(array) - 1
	pointer2 = None
	while pointer1 > 0:
		if array[pointer1] != toMove:
			pointer2 = pointer2 if pointer2 is not None else pointer1
			while pointer2 >= 0 and array[pointer2] != toMove:
				pointer2 -= 1
			if pointer2 >= 0:
				array[pointer1], array[pointer2] = array[pointer2], array[pointer1]
			else:
				break
		pointer1 -= 1
	return array