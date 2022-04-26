import math


def encryption(s):
    s = s.replace(' ', '')
    upper_border = math.ceil(math.sqrt(len(s)))
    encrypted_parts = []
    for i in range(0, upper_border):
        part = ""
        for j in range(0, upper_border):
            idx = i + j * upper_border
            if idx < len(s):
                part += s[idx]
        encrypted_parts.append(part)
    return " ".join(encrypted_parts)

