def str_joker(text, pattern):
    results = []
    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if pattern[j] != '?' and text[i+j] != pattern[j]:
                break
        else:
            results.append(str(i))
    return results


if __name__ == '__main__':
    results = ''
    for _ in range(int(input())):
        text = input()
        pattern = input()
        res = str_joker(text, pattern)
        results += str(len(res)) + '\n' + ' '.join(res) + '\n'
    print(results)