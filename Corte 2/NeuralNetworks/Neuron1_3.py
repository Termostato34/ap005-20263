# --- Datos ---
inputs = [1, 2, 3, 4]
targets = [4, 6, 8, 10]    # Ahora la relación es y = 2x + 2: la recta ya no pasa por el origen

# --- Hiperparámetros ---
w = 0.1                    # Peso inicial (pendiente); valor correcto: 2
b = 0.3                    # Sesgo inicial (ordenada al origen); valor correcto: 2
epochs = 300               # Más épocas porque hay dos parámetros y converge más lento
learning_rate = 0.1

# --- Modelo ---
def predict(i):
  return w*i + b           # Recta completa: y_pred = w*x + b

# --- Entrenamiento ---
for _ in range(epochs):
  pred = [predict(i) for i in inputs]                          # Predicciones con w y b actuales
  errors = [(p - t)**2 for p, t in zip(pred, targets)]         # Error cuadrático por muestra
  cost = sum(errors)/len(targets)                              # MSE, solo para monitorear

  ##########################################################
  # Gradientes de cada parámetro
  errors_d = [2*(p - t) for p, t in zip(pred, targets)]        # d(error²)/d(pred), común a w y b
  weight_d = [e*i for e, i in zip(errors_d, inputs)]           # Gradiente de w: d(pred)/dw = x
  bias_d = [e*1 for e in errors_d]                             # Gradiente de b: d(pred)/db = 1, por eso se multiplica por 1
  w -= learning_rate*sum(weight_d)/len(weight_d)               # Actualiza w con su gradiente promedio
  b -= learning_rate*sum(bias_d)/len(bias_d)                   # Actualiza b con su gradiente promedio
  ##########################################################

  print(f"Weight: {w: .2f}, Bias: {b:.2f}, Cost: {cost:.2f}")  # Ambos parámetros y el costo de esta época

# --- Prueba ---
test_inputs = [5, 6]
test_targets = [10, 12]
pred = [predict(i) for i in test_inputs]
for i, t, p in zip(test_inputs, test_targets, pred):
  print(f"input:{i}, target:{t}, pred:{p:.4f}")
