import math

def relu(x):
    return max(x, 0)

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def dense_layer(inputs, weights, biases, activation):
    outputs = []
    
    for neuron_weights, bias in zip (weights, biases):
        z = 0
        for i, w in zip(inputs, neuron_weights):
            z += i*w
            
            z += bias
            outputs.append(activation(z))
            
    return outputs

# Input
inputs = [0.5, -0.3, 0.8]

# Layer 1
weights1 = [
    [0.2, 0.8, -0.5],
    [0.7, -0.1, 0.3],
    [-0.3, 0.6, 0.9],
    [0.5, -0.4, 0.2]
]
biases1 = [0.1, -0.2, 0.05, 0.3]

# Layer 2
weights2 = [
    [0.6, -0.3, 0.2, 0.8],
    [-0.5, 0.7, -0.1, 0.4]
]
biases2 = [0.2, -0.1]


# Forward pass
layer1_output = dense_layer(inputs, weights1, biases1, relu)
print("Layer 1 Output:", layer1_output)

layer2_output = dense_layer(layer1_output, weights2, biases2, relu)
print("Final Output:", layer2_output)