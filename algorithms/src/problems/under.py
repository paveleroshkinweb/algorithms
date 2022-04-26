def underscorifySubstring(string, substring):
	indexes = []
	i = 0
	while i < len(string):
		substr_index = string.find(substring, i)
		if substr_index == -1:
			break
		indexes.append([substr_index, substr_index + len(substring)])
		i = substr_index + 1

	if not indexes:
		return string

	collapsed_indexes = [indexes[0]]
	for i in range(1, len(indexes)):
		if indexes[i][0] <= collapsed_indexes[-1][1]:
			collapsed_indexes[-1][1] = indexes[i][1]
		else:
			collapsed_indexes.append(indexes[i])

	result = []
	idx = 0
	for i in range(len(string) + 1):
		if idx < len(collapsed_indexes) and collapsed_indexes[idx][0] == i:
			result.append('_')
		if idx < len(collapsed_indexes) and collapsed_indexes[idx][1] == i:
			result.append('_')
			idx += 1
		if i < len(string):
			result.append(string[i])
	return "".join(result)


print(underscorifySubstring("testest", 'test'))
