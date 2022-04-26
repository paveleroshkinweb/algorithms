def validStartingCity(distances, fuel, mpg):
    length = len(distances)
    passes = [fuel[i] * mpg - distances[i] for i in range(length)]
    result = 0
    current_sum = 0
    for i in range(length - 1):
        current_sum += passes[i]
        if current_sum < 0:
            current_sum = 0
            result = i + 1
    return result
