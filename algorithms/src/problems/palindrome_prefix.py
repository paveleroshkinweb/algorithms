def find_max_palindrome_prefix(s):
    max_prefix = 0
    for i in range(1, len(s) + 1):
        substr = s[:i]
        if substr == substr[::-1]:
            max_prefix = i
    return max_prefix


if __name__ == '__main__':
    results = ''
    for _ in range(int(input())):
        results += str(find_max_palindrome_prefix(input())) + '\n'
    print(results, sep='')