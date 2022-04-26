def generateDivTags(numberOfTags):
	if numberOfTags == 1:
		return ["<div></div>"]
	result = set()
	child_divs = generateDivTags(numberOfTags - 1)
	for child_div in child_divs:
		result.add(f'<div>{child_div}</div>')
		result.add(f'<div></div>{child_div}')
		result.add(f'{child_div}<div></div>')
	return list(result)



print(generateDivTags(3))

arr1 = ["<div><div><div><div></div></div></div></div>", "<div><div><div></div><div></div></div></div>", "<div><div><div></div></div><div></div></div>", "<div><div><div></div></div></div><div></div>", "<div><div></div><div><div></div></div></div>", "<div><div></div><div></div><div></div></div>", "<div><div></div><div></div></div><div></div>", "<div><div></div></div><div><div></div></div>", "<div><div></div></div><div></div><div></div>", "<div></div><div><div><div></div></div></div>", "<div></div><div><div></div><div></div></div>", "<div></div><div><div></div></div><div></div>", "<div></div><div></div><div><div></div></div>", "<div></div><div></div><div></div><div></div>"]
arr2 = ["<div></div><div></div><div></div><div></div>", "<div><div></div><div></div><div></div></div>", "<div><div></div><div><div></div></div></div>", "<div><div><div></div><div></div></div></div>", "<div></div><div></div><div><div></div></div>", "<div><div><div></div></div></div><div></div>", "<div></div><div><div></div><div></div></div>", "<div><div><div></div></div><div></div></div>", "<div><div><div><div></div></div></div></div>", "<div><div></div><div></div></div><div></div>", "<div></div><div><div></div></div><div></div>", "<div><div></div></div><div></div><div></div>", "<div></div><div><div><div></div></div></div>"]

[print(el) for el in arr1 if el not in arr2]