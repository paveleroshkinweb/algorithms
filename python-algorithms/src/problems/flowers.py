def count_flowers(flowers):
    flowers.sort()
    if flowers[0] == flowers[-1]:
        l = len(flowers)
        return 0, int(l*(l-1)/2)
    left_part = right_part = 1
    while flowers[left_part] == flowers[0]:
        left_part += 1
    while flowers[-1-right_part] == flowers[-1]:
        right_part += 1
    return flowers[-1] - flowers[0], left_part * right_part


if __name__ == '__main__':
    _ = input()
    flowers = [int(flower) for flower in input().split()]
    max_diff, count = count_flowers(flowers)
    print(f'{max_diff} {count}', sep='')