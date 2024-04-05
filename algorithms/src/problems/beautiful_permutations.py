def construct_permutation(n):

    if n == 1:
        return [1]

    if n <= 3:
        return None

    permutation = []

    last_odd_idx = ((n - 1) // 2) + 1
    last_even_idx = n - last_odd_idx

    if last_odd_idx == last_even_idx:

        for i in range(1, last_even_idx + 1):
            permutation.append(2 * i)

        for i in range(1, last_odd_idx + 1):
            permutation.append(2 * i - 1)

    else:

        for i in range(1, last_odd_idx + 1):
            permutation.append(2 * i - 1)

        for i in range(1, last_even_idx + 1):
            permutation.append(2 * i)
    
    return permutation


if __name__ == '__main__':

    n = int(input())
    permutation = construct_permutation(n)
    if permutation is None:
        print("NO SOLUTION")
    else:
        print(*map(str, permutation))
