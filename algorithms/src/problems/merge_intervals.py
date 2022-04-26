def mergeOverlappingIntervals(intervals):
	if len(intervals) <= 1:
		return intervals
    intervals.sort(key=lambda interval: (interval[0], interval[1]))
	merged_intervals = [intervals[0]]
	for i in range(1, len(intervals)):
		if merged_intervals[-1][0] <= intervals[i][0] <= merged_intervals[-1][1]:
			merged_intervals[-1] = [merged_intervals[-1][0], max(intervals[i][1], merged_intervals[-1][1])]
		else:
			merged_intervals.append(intervals[i])
	return merged_intervals