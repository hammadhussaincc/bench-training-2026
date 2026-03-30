import math

def sigmoid_activation(x):
    return 1 / (1 + math.exp(-x))

def relu_activation(x):
    return max(0, x)

def neuron(inputs, weights, bias, activation_function):
    weighted_sum = sum([i*w for i,w in zip(inputs, weights)]) + bias
    print(f"sum: {weighted_sum}")
    output = activation_function(weighted_sum)
    print(f"output: {output}")
    return output

# Example Inputs and Weights
inputs = [0.5, -1.5, 2.0]  # Example input values (list of floats)
weights = [0.8, -0.3, 1.2]  # Example weight values (list of floats)
bias = 0.5

# Test Sigmoid Activation
sigmoid_output = neuron(inputs, weights, bias, sigmoid_activation)
print("Output with Sigmoid activation:", sigmoid_output)

# Test ReLU Activation
relu_output = neuron(inputs, weights, bias, relu_activation)
print("Output with ReLU activation:", relu_output)