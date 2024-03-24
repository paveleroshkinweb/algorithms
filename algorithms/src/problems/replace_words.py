def shortify(words, dictionary):
    new_words = []
    for word in words:

        for i in range(1, len(word)+1):

            prefix = word[:i]

            if prefix in dictionary:
                new_words.append(prefix)
                break
        else:
            new_words.append(word)

    return new_words


if __name__ == '__main__':

    dictionary = set(input().split())
    words = list(input().split())

    new_words = shortify(words, dictionary)

    print(*new_words)
