def find_longest_seq(dna_sequence):
    prev_element = dna_sequence[0]
    current_subseq = 1
    longest_subseq = 1
    for idx in range(1, len(dna_sequence)):
        
        if dna_sequence[idx] == prev_element:
            current_subseq += 1
        else:
            longest_subseq = max(longest_subseq, current_subseq)
            current_subseq = 1
            prev_element = dna_sequence[idx]

    return max(longest_subseq, current_subseq)


if __name__ == '__main__':
    dna_sequence = input()
    best_seq = find_longest_seq(dna_sequence)
    print(best_seq)
