# --- Datos ---
inputs = [1, 2, 3, 4]      # Valores de entrada x
targets = [2, 4, 6, 8]     # Salidas deseadas; la relación real es y = 2x, así que w debería llegar a 2

# --- Hiperparámetros ---
w = 0.1                    # Peso inicial, un valor arbitrario (la respuesta correcta es 2)
learning_rate = 0.1        # Factor que controla cuánto se corrige w en cada iteración

# --- Modelo ---
def predict(i):
  return w*i               # Modelo lineal sin sesgo: y_pred = w * x. Usa la variable global w, por eso ve sus actualizaciones

# --- Entrenamiento ---
for _ in range(30):                                        # 30 épocas; "_" indica que el contador no se usa
  pred = [predict(i) for i in inputs]                      # Predicción del modelo para cada entrada con el w actual
  errors = [t - p for p, t in zip(pred, targets)]          # Error de cada muestra: objetivo - predicción (con signo)
  cost = sum(errors)/len(targets)                          # Error promedio; positivo si el modelo se queda corto, negativo si se pasa
  print(f"Targets: ", targets)                             # Muestra los objetivos
  print(f"Predictions: ", pred)                            # Muestra las predicciones actuales
  print(f"Errors: ", errors)                               # Muestra el error de cada muestra
  print(f"Weight: {w: .10f}, Cost: {cost:.6f}")            # Peso con 10 decimales (el espacio deja lugar al signo) y costo con 6
  w += learning_rate*cost                                  # Si cost > 0, w sube; si cost < 0, w baja

# --- Prueba con datos que el modelo no vio ---
test_inputs = [5, 6]
test_targets = [10, 12]
pred = [predict(i) for i in test_inputs]                   # Predice con el w ya entrenado
for i, t, p in zip(test_inputs, test_targets, pred):       # Recorre entrada, objetivo y predicción a la vez
  print(f"input:{i}, target:{t}, pred:{p:.4f}")            # Compara predicción y objetivo
