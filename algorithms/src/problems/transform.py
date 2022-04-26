def transformSentence(sentence):
    words = sentence.split(' ')
    transformed = []
    for word in words:
        result = word[0]
        for i in range(1, len(word)):
            lower_next = word[i].lower()
            lower_prev = word[i - 1].lower()
            if lower_next == lower_prev:
                result += word[i]
            elif lower_next < lower_prev:
                result += word[i].upper()
            else:
                result += word[i].lower()
        transformed.append(result)
    return " ".join(transformed)


if __name__ == '__main__':
    sentence = input()
    result = transformSentence(sentence)
    print(result)