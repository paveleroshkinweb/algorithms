def find_max_books(time, books):
    length = len(books)
    sum_cache = get_sum_cache(books, length)
    if sum_cache[0] <= time:
        return length
    max_books = binary_search(0, length-1, time, sum_cache)
    i = 1
    while i < len(books) - max_books:
        if sum_cache[i-1] - sum_cache[min(i+max_books, length)] >= \
                sum_cache[i] - sum_cache[min(i+max_books+1, length)]:
            max_books = max(max_books, binary_search(i, length-1, time, sum_cache))
        i += 1
    return max_books


def get_sum_cache(books, length):
    sum_cache = [sum(books)]
    for i in range(1, length):
        sum_cache.append(sum_cache[i-1] - books[i-1])
    sum_cache.append(0)
    return sum_cache


def binary_search(i, j, time, cache):
    left = i
    right = j
    solution = 0
    while left <= right:
        middle = (left + right) // 2
        curr_sum = cache[i] - cache[middle+1]
        if curr_sum <= time:
            solution = max(solution, middle - i + 1)
            left = middle + 1
        else:
            right = middle - 1
    return solution


if __name__ == '__main__':
    _, time = [int(e) for e in input().split()]
    books = [int(e) for e in input().split()]
    print(find_max_books(time, books))