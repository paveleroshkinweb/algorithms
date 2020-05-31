import math

n_trips, n_card, cost_trip, cost_card = [int(s) for s in input().split()]


def find_min_cost(n_trips, n_card, cost_trip, cost_card):
    if cost_card / n_card >= cost_trip:
        return n_trips * cost_trip
    min_cost = min(math.ceil(n_trips / n_card) * cost_card,
                   n_trips // n_card * cost_card + (n_trips - n_trips // n_card * n_card) * cost_trip)
    return min_cost


min_cost = find_min_cost(n_trips, n_card, cost_trip, cost_card)
print(min_cost)
