def nonConstructibleChange(coins):
	coins.sort()
	current_sum = 0
	for coin in coins:
		if coin > current_sum + 1:
			break
		current_sum += coin
	return current_sum + 1