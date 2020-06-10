import numpy as np


def neural_network(input_data, weights):
    return weights.dot(input_data)


def gradient_descent(input_data, weights, goal_prediction):
    alpha = .01
    prediction = neural_network(input_data, weights)
    while (prediction - goal_prediction) ** 2 > .00001:
        direction_and_amount = prediction - goal_prediction
        weights -= np.array([direction_and_amount * data * alpha for data in input_data])
        prediction = neural_network(input_data, weights)
    return weights


if __name__ == '__main__':
    weights = np.array([0.1, 0.2, -0.1])
    input_data = np.array([5, 0.6, 7])
    print(gradient_descent(input_data, weights, 8))
