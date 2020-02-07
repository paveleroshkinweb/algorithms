def adjustment_weight(input, weight, goal_prediction, iteration_count=12000, alpha=.01):
    for _ in range(iteration_count):
        pred = prediction(input, weight)
        direction_and_amount = (pred - goal_prediction) * input
        weight -= direction_and_amount * alpha
    return weight


def prediction(input, weight):
    return input * weight


weight = .5
goal_prediction = .8
input = .5

weight = adjustment_weight(input, weight, goal_prediction)
pred = prediction(input, weight)

assert .2 > abs(pred - goal_prediction)
