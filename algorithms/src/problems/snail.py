def find_best_combination(foods: list[tuple[int]]):
    profit = []
    loss = []
    max_profit_idx = None
    max_profit_with_loss_idx = None
    
    for food in foods:

        weights = food[1]

        if weights[0] - weights[1] >= 0:
            profit.append(food)
        else:
            loss.append(food)

            if max_profit_with_loss_idx is None:
                max_profit_with_loss_idx = len(loss) - 1
            elif loss[max_profit_with_loss_idx][1][0] < weights[0]:
                max_profit_with_loss_idx = len(loss) - 1

    diff_sum = sum(food[1][0] - food[1][1] for food in profit)

    for idx, food_with_profit in enumerate(profit):

        weights = food_with_profit[1]

        if max_profit_idx is None:
            max_profit_idx = idx
        
        elif diff_sum + weights[1] > diff_sum + profit[max_profit_idx][1][1]:
            max_profit_idx = idx

    if max_profit_idx is not None:
        profit[len(profit)-1], profit[max_profit_idx] = profit[max_profit_idx], profit[len(profit)-1]

    if max_profit_with_loss_idx is not None:
        loss[0], loss[max_profit_with_loss_idx] = loss[max_profit_with_loss_idx], loss[0]

    best_combination = []
    max_height = 0
    current_hieght = 0
    drop = 0

    for day, weights in (profit + loss):
        current_hieght = current_hieght + weights[0] - drop
        best_combination.append(day)
        max_height = max(max_height, current_hieght)
        drop = weights[1]

    return max_height, best_combination


if __name__ == '__main__':
    foods = []
    for i in range(int(input())):
        up, down = list(map(int, input().split()))
        foods.append((i + 1, (up, down)))
    height, comb = find_best_combination(foods)
    print(height)
    print(' '.join(map(str, comb)))
