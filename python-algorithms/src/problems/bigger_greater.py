def biggerIsGreater(word):
    if len(word) <= 1:
        return 'no answer'
    i = len(word) - 1
    char_arr = list(word)
    while i >= 1 and char_arr[i] <= char_arr[i-1]:
        i -= 1
    if i == 0:
        return 'no answer'
    counter = len(word) - 1
    index = i
    for idx in range((len(word) - i) // 2):
        char_arr[index], char_arr[counter] = char_arr[counter], char_arr[index]
        index += 1
        counter -= 1
    for idx in range(i, len(word)):
        if char_arr[i-1] < char_arr[idx]:
            char_arr[i-1], char_arr[idx] = char_arr[idx], char_arr[i-1]
            break
    return "".join(char_arr)

