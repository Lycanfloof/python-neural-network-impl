import numpy as np

class Layer:
  def __init__(self) -> None:
    self.input = None
    self.output = None

  def forward_propagation(self, input) -> np.ndarray:
    raise NotImplementedError

  def backward_propagation(self, cost, learning_rate) -> np.ndarray:
    raise NotImplementedError