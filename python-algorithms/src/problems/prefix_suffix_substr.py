def find_prefix_suffix_substr(s):
    prefixes = get_all_prefixes(s)
    suffixes = get_all_suffixes(s)
    intersection = prefixes.intersection(suffixes)
    pref_suff = prefixes | suffixes
    count = 0
    for i in range(0, len(s)+1):
        for j in range(i+1, len(s)+1):
            substr = s[i:j]
            if substr not in intersection and substr in pref_suff:
                count += 1
    return count


def get_all_prefixes(s):
    prefixes = set()
    for i in range(1, len(s)):
        prefixes.add(s[:i])
    return prefixes


def get_all_suffixes(s):
    suffixes = set()
    for i in range(1, len(s)):
        suffixes.add(s[len(s)-i:len(s)])
    return suffixes


if __name__ == '__main__':
    results = ''
    for _ in range(int(input())):
        results += str(find_prefix_suffix_substr(input())) + '\n'
    print(results, sep='')
