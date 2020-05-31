length = int(input().strip())
lamps = sorted([int(lamp) for lamp in input().split()])

original_max_distance = max_distance = max(lamps[0], length - lamps[-1])

for i in range(1, len(lamps)):
    max_distance = max(max_distance, lamps[i] - lamps[i-1])

print(max(original_max_distance, max_distance / 2))
