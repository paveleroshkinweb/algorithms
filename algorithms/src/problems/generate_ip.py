def validIPAddresses(string):
    if len(string) < 4 or string[0] == 0:
        return []
    return generate(string, 4)


def generate(string, parts):
    if parts > 0 and not string:
        return None
    if parts == 1:
        if len(string) > 1 and string[0] == 0 or not is_valid_part(string):
            return None
        return [string]
    ip_addresses = []
    border = 3 if len(string) >= 3 else len(string)
    for i in range(border):
        part = string[0:i+1]
        if is_valid_part(part):
            child_parts = generate(string[i+1:], parts-1)
            if child_parts:
                for child in child_parts:
                    ip_addresses.append(f'{part}.{child}')
    return ip_addresses


def is_valid_part(part):
	number = int(part)
	if number > 255:
		return False
	return len(str(number)) == len(part)
