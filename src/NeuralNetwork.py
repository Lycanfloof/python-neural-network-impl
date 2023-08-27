import numpy as np

class NeuralNetwork:
  def __init__(self, cost_function, cost_prime, layers = []) -> None:
    self.cost_function = cost_function
    self.cost_prime = cost_prime
    self.layers = layers

  def set_layers(self, layers) -> None:
    self.layers = layers

  def add_layer(self, layer) -> None:
    self.layers.append(layer)

  def fit(self, x_train, y_train, epochs = 50, verbose = False, learning_rate = 0.1) -> None:
    for epoch in range(epochs):
      output = self.__forward_propagation(x_train)

      if verbose: print("Epoch: {} -> Cost: {}".format(epoch + 1, self.cost_function(output, y_train)))

      cost = self.cost_prime(output, y_train)
      self.__backward_propagation(cost, learning_rate)

  def predict(self, x) -> np.ndarray:
    return self.__forward_propagation(x)

  def __forward_propagation(self, x) -> np.ndarray:
    layer_output = x

    for layer in self.layers:
      layer_output = layer.forward_propagation(layer_output)

    return layer_output

  def __backward_propagation(self, cost, learning_rate) -> None:
    current_cost = cost

    for layer in reversed(self.layers):
      current_cost = layer.backward_propagation(current_cost, learning_rate)