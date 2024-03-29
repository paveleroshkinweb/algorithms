def calculate_occupied_fields2(k):
    ships_n = (k * (k+1)) // 2
    extra = ((k-1) * k * (k+1)) // 3
    fields = k * ships_n - extra + (ships_n - 1)
    return fields


def find_best_ship_size(n):
    left = 1
    right = n

    while left <= right:

        middle = (left + right) // 2
        fields = calculate_occupied_fields2(middle)

        if fields == n:
            return middle

        if fields < n:
            left = middle + 1
        else:
            right = middle - 1

    return left - 1


if __name__ == '__main__':

    n = int(input())
    best_size = find_best_ship_size(n)
    print(best_size)