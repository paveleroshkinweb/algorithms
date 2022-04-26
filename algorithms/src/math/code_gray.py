def code_gray(length):
    assert length >= 0
    if length == 0:
        return []
    if length == 1:
        return ['0', '1']
    codes = code_gray(length - 1)
    gray_codes = []
    for code in codes:
        gray_codes.append(code + '0')
    for code in reversed(codes):
        gray_codes.append(code + '1')
    return gray_codes

