import time
import numpy as np
import matplotlib.pyplot as plt

inputs = np.array([1, 2, 3, 4], dtype=float)
targets = np.array([2, 4, 6, 8], dtype=float)

w = 0.1
epochs = 10
learning_rate = 0.1
pause_time = 0

weight_history = []
cost_history = []

for epoch in range(epochs):
    predictions = w * inputs
    errors = (predictions - targets) ** 2
    cost = np.mean(errors)
    
    errors_d = 2 * (predictions - targets)
    weight_d = errors_d * inputs
    gradient = np.mean(weight_d)
    
    w -= learning_rate * gradient
    
    weight_history.append(w)
    cost_history.append(cost)
    time.sleep(pause_time)

plt.figure(figsize=(8, 4))
plt.plot(range(1, epochs + 1), cost_history, marker="o", color="purple")
plt.xlabel("Época")
plt.ylabel("Costo J")
plt.title("Evolución de la Función de Costo J")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(range(1, epochs + 1), weight_history, marker="o", color="green")
plt.xlabel("Época")
plt.ylabel("Peso w")
plt.title("Ajuste del Peso w por Descenso por Gradiente")
plt.grid(True)
plt.show()
