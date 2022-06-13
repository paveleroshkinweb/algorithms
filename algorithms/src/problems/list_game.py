def list_game(length, total_sum):
    if total_sum >= 2 * length:
        remainder = total_sum - 2 * length
        arr = [2] * length
        arr[-1] += remainder
        return "YES", " ".join(map(str, arr)), "1"
    return "NO",
    