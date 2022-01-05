def firstNonRepeatingCharacter(string):
	if len(string) == 0:
		return -1
	d = {}
	for idx, char in enumerate(string):
		if char in d:
			d[char] = float('inf')
		else:
			d[char] = idx
	res = min([idx for idx in d.values()])
	if res == float('inf'):
		return -1
	return res