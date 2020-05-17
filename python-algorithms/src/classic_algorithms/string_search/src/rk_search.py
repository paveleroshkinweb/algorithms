def rk_search(string, substring):
    assert len(string) >= len(substring)
    r = 256
    q = 15487469
    substring_hash = hash(substring, len(substring), r, q)
    text_hash = hash(string, len(substring), r, q)
    rm = get_rm(len(substring), r, q)
    if substring_hash == text_hash:
        return 0
    for i in range(len(substring), len(string)):
        text_hash = (text_hash + q - rm * ord(string[i-len(substring)]) % q) % q
        text_hash = (text_hash * r + ord(string[i])) % q
        if text_hash == substring_hash and substring == string[i - len(substring) + 1: i + 1]:
            return i - len(substring) + 1
    return -1


def get_rm(length, r, q):
    rm = 1
    for i in range(1, length):
        rm = (r * rm) % q
    return rm


def hash(string, m, r, q):
    h = 0
    for i in range(m):
        h = (r * h + ord(string[i])) % q
    return h
