def reverseWordsInString(string):
    reversed_words = ""
    i = 0
    while i < len(string):
        if string[i] == ' ':
            reversed_words = string[i] + reversed_words
            i += 1
        else:
            last_word = ''
            while i < len(string) and string[i] != ' ':
                last_word += string[i]
                i += 1
            reversed_words = last_word + reversed_words

    return reversed_words

