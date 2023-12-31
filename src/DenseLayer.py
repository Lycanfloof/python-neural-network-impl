import numpy as np
from Layer import Layer

class DenseLayer(Layer):
  def __init__(self, input_size, output_size, seed = 42) -> None:
    super().__init__()
    np.random.seed(seed)
    self.weights = np.random.rand(output_size, input_size) - 0.5
    self.bias = np.random.rand(output_size, 1) - 0.5

  def forward_propagation(self, input) -> np.ndarray:
    self.input = input
    self.output = np.dot(self.weights, input) + self.bias

    return self.output

  def backward_propagation(self, cost, learning_rate) -> np.ndarray:
    weights_cost = np.dot(cost, self.input.transpose())

    self.weights -= learning_rate * weights_cost
    self.bias -= learning_rate * np.sum(cost, 1, keepdims = True)

    return np.dot(self.weights.transpose(), cost)