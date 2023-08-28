import numpy as np

def mse(y_hat, y):
  return 1 / y.shape[1] * np.sum(np.square(y_hat - y), keepdims = True)

def mse_prime(y_hat, y):
  return 2 / y.shape[1] * (y_hat - y)

def binary_cross_entropy(y_hat, y):
  return -1 / y.shape[1] * np.sum((y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat)), keepdims = True)

def binary_cross_entropy_prime(y_hat, y):
  return 1 / y.shape[1] * (y_hat - y) / (y_hat * (1 - y_hat))

def sigmoid(z):
  return 1 / (1 + np.exp(-z))

def sigmoid_prime(z):
  return np.exp(-z) / np.square(1 + np.exp(-z))

def relu(z):
  return np.maximum(0, z)

def relu_prime(z):
  return (z > 0).astype(int)

def tanh(z):
  return np.tanh(z)

def tanh_prime(z):
  return 1 - np.square(np.tanh(z))