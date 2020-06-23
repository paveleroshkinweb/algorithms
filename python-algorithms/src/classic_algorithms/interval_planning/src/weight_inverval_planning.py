from functools import lru_cache


def weight_interval_planning(intervals):

    @lru_cache(1000)
    def weight_interval_planning_helper(index):
        if index == -1:
            return 0
        return max(
            sorted_intervals[index][1] + weight_interval_planning_helper(prev_intervals[index]),
            weight_interval_planning_helper(index - 1)
        )

    sorted_intervals = sorted(intervals, key=lambda interval_weight: interval_weight[0][1])
    prev_intervals = get_prev_intervals(sorted_intervals)
    return weight_interval_planning_helper(len(intervals) - 1)


def get_prev_intervals(intervals):
    prev_intervals = []
    for i in range(len(intervals)):
        for j in range(i-1, -1, -1):
            if intervals[i][0][0] > intervals[j][0][1]:
                prev_intervals.append(j)
                break
        else:
            prev_intervals.append(-1)
    return prev_intervals


intervals1 = [
    ((1, 2), 3),
    ((1.5, 3), 4),
    ((3.5, 5), 6),
    ((4, 4.5), 2),
    ((4.25, 6), 1),
    ((4.5, 7), 5),
    ((5.5, 9), 7),
]

intervals2 = [
    ((1, 3), 7),
    ((2, 4), 3),
    ((2.5, 5), 10),
    ((4, 10), 5)
]

print(weight_interval_planning(intervals1))