def min_steps_to_destroy_helper(x, y, soldiers, p):

    if x <= 0:
        return float('inf')

    if y <= 0 and soldiers <= 0:
        return 0

    if y > x:
        # We can't destroy the barrack but we can kill all soldiers
        soldiers1 = 0
        y1 = y - (x - soldiers)
        if y1 > 0:
            soldiers1 += p
        return 1 + min_steps_to_destroy_helper(x, y1, soldiers1, p)

    # Hit barrack first
    y2 = 0
    soldiers2 = soldiers - (x - y)
    x2 = x - soldiers2

    # Try to hit soldiers first
    if x >= soldiers:
        soldiers3 = 0
        y3 = y - (x - soldiers)
        if y3 > 0:
            soldiers3 += p
        
        if y3 + soldiers3 < y + soldiers:

            return 1 + min(
                min_steps_to_destroy_helper(x2, y2, soldiers2, p),
                min_steps_to_destroy_helper(x, y3, soldiers3, p)
            )

    return 1 + min_steps_to_destroy_helper(x2, y2, soldiers2, p)


def min_steps_to_destroy(x, y, p):
    y -= x

    if y <= 0:
        return 1

    if y >= x and p >= x:
        return -1

    res = 1 + min_steps_to_destroy_helper(x, y, p, p)
    
    if res == float('inf'):
        return -1
    return res


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    p = int(input())
    steps = min_steps_to_destroy(x, y, p)
    print(steps)
