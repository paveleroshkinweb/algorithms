def paint(P, V, Q, M):
    L1 = P - V
    R1 = P + V
    L2 = Q - M
    R2 = Q + M
    
    is_intersection = (L2 <= R1 and L1 <= L2) or (L1 <= R2 and L1 >= L2)
    if is_intersection:
        min_left = min(L1, L2)
        max_right = max(R1, R2)
        return max_right - min_left + 1

    return (1 + 2 * V) + (1 + 2 * M)


if __name__ == '__main__':
    P, V = list(map(int, input().split()))
    Q, M = list(map(int, input().split()))
    n = paint(P, V, Q, M)
    print(n)
