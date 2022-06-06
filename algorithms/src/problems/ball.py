from collections import defaultdict

def count_pairs(pairs):
    pairs_length = len(pairs)
    man_pairs = defaultdict(lambda: 0)
    woman_pairs = defaultdict(lambda: 0)
    count = 0
    for man, woman in pairs:
        man_pairs[man] += 1
        woman_pairs[woman] += 1
    for man, woman in pairs:
        suitable_pairs = pairs_length - man_pairs[man] - woman_pairs[woman] + 1
        count += suitable_pairs
    return count // 2


if __name__ == '__main__':
    results = []
    for _ in range(int(input())):
        man_n, woman_n, _ = [int(s) for s in input().split(' ')]
        man = [int(s) for s in input().split(' ')]
        woman = [int(s) for s in input().split(' ')]
        pairs = list(zip(man, woman))
        results.append(str(count_pairs(pairs)))
    print("\n".join(results))
