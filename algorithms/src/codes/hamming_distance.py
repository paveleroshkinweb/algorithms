def hamming_distance(word1: int, word2: int):
    unmatched_positions = word1 ^ word2
    distance = 0
    while unmatched_positions:
        unmatched_positions = unmatched_positions & (unmatched_positions - 1)
        distance += 1
    return distance
