from collections import defaultdict


def minimumCharactersForWords(words):
    global_letters_map = defaultdict(lambda: 0)
    for word in words:
        letters_map = get_letters_map(word)
        merge_maps(global_letters_map, letters_map)
    min_characters = []
    for char, count in global_letters_map.items():
        min_characters += [char] * count
    return min_characters


def get_letters_map(word):
    letters = defaultdict(lambda: 0)
    for char in word:
        letters[char] += 1
    return letters


def merge_maps(global_map, local_map):
    for key in local_map:
        global_map[key] = max(global_map[key], local_map[key])
