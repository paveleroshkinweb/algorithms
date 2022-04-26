import numpy as np


def neural_network(input_data, weights):
    hid = input_data.dot(weights[0])
    pred = hid.dot(weights[1])
    return pred


ih_wgt = np.array([
    [0.1, 0.2, -0.1],
    [-0.1, 0.1, 0.9],
    [0.1, 0.4, 0.1]]).T

hp_wgt = np.array([
    [0.3, 1.1, -0.3],
    [0.1, 0.2, 0.0],
    [0.0, 1.3, 0.1]]).T

weights = [ih_wgt, hp_wgt]

toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])

inputs = [np.array(input_data) for input_data in zip(toes, wlrec, nfans)]

for input_data in inputs:
    prediction = neural_network(input_data, weights)
    print(prediction)


