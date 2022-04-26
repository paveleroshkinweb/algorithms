def caesarCipherEncryptor(string, key):
	key = key % 26
    encrypted_string = ""
	for char in string:
		code = (ord(char) + key)
		if code > 122:
			code = 96 + (code % 122)
		encrypted_string += chr(code)
	return encrypted_string