def highest_profit(data):

    def highest_profit_helper(data):
        if len(data) <= 1:
            return 0, data[0], data[0]
        middle = len(data) // 2
        left_data, right_data = data[:middle], data[middle:]
        left_highest_profit, max_left, min_left = highest_profit_helper(left_data)
        right_highest_profit, max_right, min_right = highest_profit_helper(right_data)
        max_profit = max(left_highest_profit, right_highest_profit, max_right - min_left)
        return max_profit, max(max_left, max_right), min(min_left, min_right)

    return highest_profit_helper(data)[0]


def brute_force(data):
    max_profit = 0
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            max_profit = max(max_profit, data[j] - data[i])
    return max_profit
