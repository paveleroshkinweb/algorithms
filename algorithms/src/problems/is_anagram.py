def _is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    from collections import Counter

    count = Counter(s1)

    for c in s2:
        if c not in count:
            return False
    
        count[c] -= 1
    
        if count[c] < 0:
            return False

    return True


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    ans = _is_anagram(s1, s2)

    if ans:
        print("YES")
    else:
        print("NO")
