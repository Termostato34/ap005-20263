import time
import numpy as np
import matplotlib.pyplot as plt

inputs = np.array([1, 2, 3, 4], dtype=float)
targets = np.array([2, 4, 6, 8], dtype=float)

w = 0.1
learning_rate = 0.1
epochs = 30
pause_time = 0

weight_history = []
error_history = []

for epoch in range(epochs):
    predictions = w * inputs
    errors = targets - predictions
    error_mean = np.mean(errors)
    
    w += learning_rate * error_mean
    
    weight_history.append(w)
    error_history.append(error_mean)
    time.sleep(pause_time)

test_inputs = np.array([5, 6], dtype=float)
test_targets = np.array([10, 12], dtype=float)
test_predictions = w * test_inputs

plt.figure(figsize=(8, 4))
plt.plot(range(1, epochs + 1), weight_history, marker="o", color="blue")
plt.xlabel("Época")
plt.ylabel("Peso w")
plt.title("Evolución del Peso w a lo largo del entrenamiento")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(range(1, epochs + 1), error_history, marker="o", color="red")
plt.xlabel("Época")
plt.ylabel("Error Promedio")
plt.title("Evolución del Error Promedio")
plt.grid(True)
plt.show()
