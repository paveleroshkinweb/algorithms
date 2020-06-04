def get_max_sum_subseq(sequence):
    max_subseq = [sequence[0]]
    for element in sequence:
        if is_different_sign(max_subseq[-1], element):
            max_subseq.append(element)
        else:
            max_subseq[-1] = max(max_subseq[-1], element)
    return sum(max_subseq)


def is_different_sign(element1, element2):
    return element2 < 0 < element1 or element1 < 0 < element2


if __name__ == '__main__':
    sequences = []
    for i in range(int(input())):
        _ = input()
        sequences.append([int(s) for s in input().split()])
    max_subseqs = [str(get_max_sum_subseq(s)) for s in sequences]
    print('\n'.join(max_subseqs), sep='')