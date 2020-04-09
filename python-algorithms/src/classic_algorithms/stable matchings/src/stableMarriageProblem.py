def stable_marriage_problem(man_preferences, girl_preferences):
    length = len(man_preferences)
    mans_indexes = [0 for _ in range(length)]
    pairs = dict([(i, None) for i in range(length)])
    available_mans = set([i for i in range(length)])
    engaged_girls = set()
    while len(available_mans) > 0:
        available_man = next(iter(available_mans))
        girl = man_preferences[available_man][mans_indexes[available_man]]
        if girl not in engaged_girls:
            pairs[available_man] = girl
            engaged_girls.add(girl)
            available_mans.remove(available_man)
        else:
            current_man = find_man(pairs, girl)
            girl_current_man_preference = girl_preferences[girl].index(current_man)
            girl_available_man_preference = girl_preferences[girl].index(available_man)
            if girl_current_man_preference > girl_available_man_preference:
                pairs[available_man] = girl
                available_mans.add(current_man)
                available_mans.remove(available_man)
                mans_indexes[current_man] += 1
            else:
                mans_indexes[available_man] += 1
    return pairs


def find_man(pairs: dict, girl):
    items = pairs.items()
    for item in items:
        if item[1] == girl:
            return item[0]
    return None
