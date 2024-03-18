def find_best_deal(k, prices):

    best_deal = 0

    for i in range(len(prices)-1):
        for j in range(i, min(i+k+1, len(prices))):
            best_deal = max(best_deal, prices[j] - prices[i])

    return best_deal


if __name__ == '__main__':
    _, k = list(map(int, input().split()))
    prices = list(map(int, input().split()))

    best_deal = find_best_deal(k, prices)
    print(best_deal)
