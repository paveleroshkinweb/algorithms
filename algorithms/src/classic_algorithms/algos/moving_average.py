from itertools import islice


def moving_average1(timeseries, k):
    normalized_timeseries = []
    for i in range(k-1, len(timeseries)):
        average = 0
        for j in range(i-k+1, i+1):
            average += timeseries[j]
        average /= k
        normalized_timeseries.append(average)

    return normalized_timeseries


def moving_average2(timeseries, k):
    normalized_timeseries = [sum(islice(timeseries, k)) / k]
    for i in range(k, len(timeseries)):
        next_average = normalized_timeseries[-1] + (timeseries[i] - timeseries[i-k]) / k
        normalized_timeseries.append(next_average)
    return normalized_timeseries
