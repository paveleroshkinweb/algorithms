def neural_network(input_data, weight):
    return input_data * weight


def naive_learning(input_data, weight, goal_prediction):
    delta = 0.01
    prediction = neural_network(input_data, weight)
    error = (goal_prediction - prediction) ** 2
    iterations = 1
    while error > .00001:
        iterations += 1
        prediction_inc_weight = neural_network(input_data, weight + delta)
        prediction_dec_weight = neural_network(input_data, weight - delta)
        new_inc_error = (goal_prediction - prediction_inc_weight) ** 2
        new_dec_error = (goal_prediction - prediction_dec_weight) ** 2
        if new_inc_error < error:
            weight += delta
            error = new_inc_error
        else:
            weight -= delta
            error = new_dec_error
    return iterations, weight


def gradient_descent(input_data, weight, goal_prediction):
    alpha = 0.1
    prediction = neural_network(input_data, weight)
    iterations = 1
    while (goal_prediction - prediction) ** 2 > .00001:
        iterations += 1
        direction_and_amount = (prediction - goal_prediction) * input_data
        weight -= direction_and_amount * alpha
        prediction = neural_network(input_data, weight)
    return iterations, weight


if __name__ == '__main__':
    input_data = 2
    weight = 0.5
    goal_prediction = 0.8
    iterations, new_weight = naive_learning(input_data, weight, goal_prediction)
    print(iterations, new_weight)
    iterations, new_weight = gradient_descent(input_data, weight, goal_prediction)
    print(iterations, new_weight)