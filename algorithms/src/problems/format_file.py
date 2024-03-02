_TAB = 4


def min_spaces_to_format(spaces):
    total_operations = 0

    for space_required in spaces:
        number_of_tabs = space_required // _TAB
        total_operations += number_of_tabs
    
        space_left = space_required % _TAB

        if space_left == 1:
            total_operations += 1
        if space_left == 2 or space_left == 3:
            total_operations += 2

    return total_operations


if __name__ == '__main__':
    spaces = []
    for _ in range(int(input())):
        spaces.append(int(input()))
    print(spaces)
    n = min_spaces_to_format(spaces)
    print(n)
