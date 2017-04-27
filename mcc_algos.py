# MCC algorithm definitions


# Algorithm 1
def changeslow(values, amount):

	min_count = amount
	min_change = [0] * len(values)

	if amount == 1:
		min_change[0] = 1
		return min_change, 1

	for i in range(len(values)):
		sub_count = amount
		if values[i] <= amount:
			(sub_change, sub_count) = changeslow(values, (amount - (values[i])))
			sub_count += 1

		if sub_count < min_count:
			min_count = sub_count
			sub_change[i] += 1
			min_change = sub_change[:]

	return min_change, min_count


# Algorithm 3: Dynamic Programming
def changedp(coins, value):
	results = []
	for i in range(len(coins)):
		results.append(0)
	
	coinTracker = []
	for i in range(value + 1):
		coinTracker.append(-1)
	
	knownCoins = []
	knownCoins.append(0)
	for i in range(1, value + 1):
		knownCoins.append(value + 1)
	
	for i in range(1, value + 1):
		minCoins = value + 1
	
		for j in range(0, len(coins)):
			if i >= coins[j]:
				minCoins = min(minCoins, knownCoins[i - coins[j]])
				
			if minCoins + 1 < knownCoins[i]:
				knownCoins[i] = minCoins + 1
				coinTracker[i] = j
	
	curIndex = len(coinTracker) - 1
	while curIndex > 0:
		results[coinTracker[curIndex]] += 1
		curIndex -= coins[coinTracker[curIndex]]
	
	return results, sum(results)
