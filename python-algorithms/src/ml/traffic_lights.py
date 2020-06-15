import numpy as np
from copy import deepcopy


def neural_network(inputs, weights):
    return inputs.dot(weights)


def gradient_descent(inputs, weights, goal_predictions, iterations=200):
    alpha = .01
    weights = deepcopy(weights)
    for _ in range(iterations):
        for goal_prediction, input in zip(goal_predictions, inputs):
            prediction = neural_network(input, weights)
            delta = prediction - goal_prediction
            weights -= delta * input * alpha
    return weights


if __name__ == '__main__':
    weights = np.random.sample(3)
    streetlights = np.array([
        [1, 0, 1],
        [0, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
        [0, 1, 1],
        [1, 0, 1]
    ])
    goal_predictions = [0, 1, 0, 1, 1, 0]
    init_predictions = neural_network(streetlights, weights)
    new_weights = gradient_descent(streetlights, weights, goal_predictions)
    new_predictions = neural_network(streetlights, new_weights)
    print(init_predictions, new_predictions)