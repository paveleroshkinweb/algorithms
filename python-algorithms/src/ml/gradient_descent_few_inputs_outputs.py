from copy import deepcopy


def neural_network(inputs, weights):
    predictions = []
    for i in range(len(weights)):
        scalar_product = 0
        for j in range(len(weights)):
            scalar_product += weights[j][i] * inputs[j]
        predictions.append(scalar_product)
    return predictions


def calculate_delta(vector1, vector2):
    assert len(vector1) == len(vector2)
    return [vector1[i] - vector2[i] for i in range(len(vector1))]


def gradient_descent(inputs, weights, goal_predictions, iterations=1000):
    alpha = 0.01
    new_weights = deepcopy(weights)
    for _ in range(iterations):
        predictions = neural_network(inputs, new_weights)
        delta = calculate_delta(predictions, goal_predictions)
        for i in range(len(delta)):
            for j in range(len(weights)):
                new_weights[j][i] -= delta[i] * inputs[j] * alpha
    return new_weights


if __name__ == '__main__':
    # Игр, побед, болельщиков
    inputs = [4, 2, 3]
    # 0 - травмы, 1 - победы, 2 - печаль
    weights = [
        [0.1, 0.8, 1.1],
        [0.2, 1.2, 2.0],
        [0.3, 0.7, 0.1]
    ]
    goal_predictions = [0.9, 0.6, 0.8]
    initial_prediction = neural_network(inputs, weights)
    new_weights = gradient_descent(inputs, weights, goal_predictions)
    new_prediction = neural_network(inputs, new_weights)
    print(initial_prediction, new_prediction)
