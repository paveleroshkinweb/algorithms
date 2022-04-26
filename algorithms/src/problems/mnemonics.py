def phoneNumberMnemonics(phoneNumber):
	letters_map = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
	mnemonics = []
	for digit in phoneNumber:
		letters = letters_map[int(digit)]
		new_mnemonics = []
		if mnemonics:
			for letter in letters:
				for mnemonic in mnemonics:
					new_mnemonics.append(mnemonic + letter)
		else:
			for letter in letters:
				new_mnemonics.append(letter)
		mnemonics = new_mnemonics
	return mnemonics
