import numpy as np
from Layer import Layer

class ActivationLayer(Layer):
  def __init__(self, activation_function, activation_prime) -> None:
    super().__init__()
    self.activation_function = activation_function
    self.activation_prime = activation_prime

  def forward_propagation(self, input) -> np.ndarray:
    self.input = input
    self.output = self.activation_function(input)

    return self.output

  def backward_propagation(self, cost, learning_rate) -> np.ndarray:
    return cost * self.activation_prime(self.input)