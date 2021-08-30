from collections import defaultdict


def find_winner(s):
    count_letters = defaultdict(lambda: 0)
    for char in s:
        count_letters[char] += 1
    even = {k: v for k, v in count_letters.items() if v & 1 == 0}
    odd = {k: v for k, v in count_letters.items() if v & 1 == 1}
    first = True
    while len(odd) > 1:
        if len(even) > 0:
            key = list(even.keys())[0]
            even[key] -= 1
            odd[key] = even[key]
            del even[key]
        else:
            key = list(odd.keys())[0]
            odd[key] -= 1
            if odd[key] > 0:
                even[key] = odd[key]
            del odd[key]
        first = not first
    return "First" if first else "Second"


if __name__ == '__main__':
    s = input()
    print(find_winner(s))