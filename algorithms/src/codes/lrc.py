def getLRC(data: bytes):
    lrc = 0
    for word in data:
        lrc ^= word
    return lrc
