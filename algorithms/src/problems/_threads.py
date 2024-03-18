def find_min_length(lengths):
    max_element = max(lengths)
    subsum = sum(lengths)

    # if subsum == max_element * 2:
    #     return max_element * 2

    # return 2 * max_element - subsum


if __name__ == '__main__':
    _ = input()
    lengths = list(map(int, input().split()))

    min_length = find_min_length(lengths)
    print(min_length)
