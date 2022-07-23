def get_shifts(sheep_row):
    sheep_count = 0
    last_sheep_position = None
    shifts = []
    for idx in range(len(sheep_row)-1, -1, -1):
        if sheep_row[idx] == '*':
            if sheep_count > 0:
                diff = last_sheep_position - idx - 1
                shift = diff * sheep_count + shifts[-1]
                shifts.append(shift)
            else:
                shifts.append(0)
            sheep_count += 1
            last_sheep_position = idx
    return list(reversed(shifts))


def sort_sheeps_min(sheep_row):
    result = float('inf')
    min_operations = 0
    shifts = get_shifts(sheep_row)
    sheep_count = 0
    last_sheep_position = -1
    for idx, item in enumerate(sheep_row):
        if item == '*':
            if sheep_count > 0:
                diff = idx - last_sheep_position - 1
                left_shift = diff * sheep_count + min_operations
                result = min(result, left_shift + shifts[sheep_count])
                min_operations = left_shift             
            last_sheep_position = idx
            sheep_count += 1
    return result if result != float('inf') else 0


if __name__ == '__main__':
    results = []
    for idx in range(int(input())):
        _ = input()
        results.append(str(sort_sheeps_min(input())))
    print("\n".join(results))
