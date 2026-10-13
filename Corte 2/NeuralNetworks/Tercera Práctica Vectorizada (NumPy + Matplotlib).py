import time
import numpy as np
import matplotlib.pyplot as plt

inputs = np.array([1, 2, 3, 4], dtype=float)
targets = np.array([4, 6, 8, 10], dtype=float)

w = 0.1
b = 0.3
epochs = 300
learning_rate = 0.1
pause_time = 0

weight_history = []
bias_history = []
cost_history = []

for epoch in range(epochs):
    predictions = w * inputs + b
    errors = (predictions - targets) ** 2
    cost = np.mean(errors)
    
    errors_d = 2 * (predictions - targets)
    weight_d = errors_d * inputs
    bias_d = errors_d
    
    gradient_w = np.mean(weight_d)
    gradient_b = np.mean(bias_d)
    
    w -= learning_rate * gradient_w
    b -= learning_rate * gradient_b
    
    weight_history.append(w)
    bias_history.append(b)
    cost_history.append(cost)
    time.sleep(pause_time)

plt.figure(figsize=(8, 4))
plt.plot(range(1, epochs + 1), cost_history, color="red")
plt.yscale("log")
plt.xlabel("Época")
plt.ylabel("Costo J (Escala Logarítmica)")
plt.title("Disminución del Costo J a lo largo de las Épocas")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(range(1, epochs + 1), weight_history, label="Peso w", color="blue")
plt.plot(range(1, epochs + 1), bias_history, label="Sesgo b", color="orange", linestyle="--")
plt.xlabel("Época")
plt.ylabel("Valor")
plt.title("Evolución de los Parámetros w y b")
plt.legend()
plt.grid(True)
plt.show()

x_plot = np.linspace(0, 7, 100)
y_plot = w * x_plot + b

plt.figure(figsize=(8, 4))
plt.scatter(inputs, targets, color="black", label="Datos de Entrenamiento")
plt.plot(x_plot, y_plot, color="green", label="Modelo Aprendido ($y = wx + b$)")
plt.xlabel("Entrada x")
plt.ylabel("Salida y")
plt.title("Ajuste Final del Modelo Neuronal a los Datos")
plt.legend()
plt.grid(True)
plt.show()
