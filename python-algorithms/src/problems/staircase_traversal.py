# O(n*k) time, O(n) space
def staircaseTraversal(height, maxSteps):
    cache = [1]
    for i in range(1, height + 1):
        current_ways = 0
        for j in range(i - 1, max(-1, i - maxSteps - 1), -1):
            current_ways += cache[j]
        cache.append(current_ways)
    return cache[-1]


# O(n) time, O(n) space
def staircaseTraversal2(height, maxSteps):
    heights = [1, 1]
    for i in range(2, height + 1):
        if i > maxSteps:
            heights.append(heights[-1] * 2 - heights[i - maxSteps - 1])
        else:
            heights.append(heights[-1] * 2)
    return heights[-1]