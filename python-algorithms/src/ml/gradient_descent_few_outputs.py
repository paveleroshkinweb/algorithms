import numpy as np


def neural_network(input, weights):
    return input * weights


def gradient(input, weights, goal_predictions, iterations=10):
    alpha = .01
    predictions = neural_network(input, weights)
    for _ in range(iterations):
        deltas = (predictions - goal_predictions) * input * alpha
        weights -= deltas
        predictions = neural_network(input, weights)
    return weights


if __name__ == '__main__':
    weights = np.array([0.1, 0.3, 0.87])
    input = 9
    goal_predictions = np.array([15.1, 19.1, 6.54])
    weights = gradient(input, weights, goal_predictions)
    print(neural_network(input, weights))
