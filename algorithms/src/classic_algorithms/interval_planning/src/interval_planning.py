from heapq import heapify, heappop, heappush


def max_independent_intervals(intervals):
    if len(intervals) <= 1:
        return intervals[:]
    intervals_queue = [(interval[1], interval) for interval in intervals]
    heapify(intervals_queue)
    independent_intervals = [heappop(intervals_queue)[1]]
    while intervals_queue:
        current_interval = heappop(intervals_queue)[1]
        if current_interval[0] >= independent_intervals[-1][1]:
            independent_intervals.append(current_interval)
    return independent_intervals


def intervals_distribution(intervals):
    if len(intervals) <= 1:
        return [intervals[:]]
    intervals_queue = [(interval[0], interval) for interval in intervals]
    heapify(intervals_queue)
    interval_groups = [[heappop(intervals_queue)[1]]]
    while intervals_queue:
        current_interval = heappop(intervals_queue)[1]
        for group in interval_groups:
            if current_interval[0] >= group[-1][1]:
                group.append(current_interval)
                break
        else:
            interval_groups.append([current_interval])
    return interval_groups


def plan_intervals(entries):
    if len(entries) <= 1:
        return entries[:]
    entries_queue = [(entry[1], entry) for entry in entries]
    heapify(entries_queue)
    intervals = [(0, heappop(entries_queue)[1][0])]
    while entries_queue:
        current_entry = heappop(entries_queue)[1]
        intervals.append(intervals[-1][1], intervals[-1][1] + current_entry[0])
    return intervals
