import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x):
    return max(0, x)


def dense_layer(inputs, weights, biases, activation):
    outputs = []

    for neuron_weights, bias in zip(weights, biases):
        weighted_sum = 0

        for i, w in zip(inputs, neuron_weights):
            weighted_sum += i * w

        weighted_sum += bias
        outputs.append(activation(weighted_sum))

    return outputs


inputs = [0.5, -1.5, 2.0]

weights = [
    [0.8, -0.3, 1.2],
    [0.1, 0.4, -0.6],
    [-0.7, 0.9, 0.2]
]

biases = [0.5, -0.2, 0.1]

print("Sigmoid:", dense_layer(inputs, weights, biases, sigmoid))
print("ReLU:", dense_layer(inputs, weights, biases, relu))