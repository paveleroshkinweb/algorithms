def minimumWaitingTime(queries):
    queries.sort()
	total = 0
	for idx, query in enumerate(queries[:-1]):
		total += query * (len(queries) - idx - 1)
	return total