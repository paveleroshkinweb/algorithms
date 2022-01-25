def powerset(array):
    if len(array) == 0:
        return [[]]
    power_set = []
    table = generate_table(len(array))
    for subtable in table:
        new_set = []
        for idx, indicator in enumerate(subtable):
            if indicator == 1:
                new_set.append(array[idx])
        power_set.append(new_set)
    return power_set


def generate_table(size):
    table = [[0], [1]]
    while size > 1:
        new_table = []
        for subtable in table:
            new_table.append(subtable + [0])
            new_table.append(subtable + [1])
        table = new_table
        size -= 1
    return table