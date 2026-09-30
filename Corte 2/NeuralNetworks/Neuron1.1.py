# --- Datos ---
inputs = [1, 2, 3, 4]
targets = [2, 4, 6, 8]     # Misma relación y = 2x

# --- Hiperparámetros ---
w = 0.1                    # Peso inicial
epochs = 10                # Ahora el número de iteraciones es un parámetro con nombre
learning_rate = 0.1

# --- Modelo ---
def predict(i):
  return w*i               # y_pred = w * x

# --- Entrenamiento ---
for _ in range(epochs):
  pred = [predict(i) for i in inputs]                          # Predicciones con el w actual
  errors = [(p - t)**2 for p, t in zip(pred, targets)]         # Error cuadrático por muestra: siempre positivo y penaliza más los errores grandes
  cost = sum(errors)/len(targets)                              # MSE (error cuadrático medio). Solo se usa para monitorear, no para actualizar w

  ##########################################################
  # Gradiente: cuánto cambia el costo si se mueve w
  errors_d = [2*(p - t) for p, t in zip(pred, targets)]        # d(error²)/d(pred) = 2(p - t). Indica cuánto cambia el error al mover la predicción
  weight_d = [e*i for e, i in zip(errors_d, inputs)]           # Regla de la cadena: d(pred)/dw = x, así que d(error²)/dw = 2(p - t)·x
  w -= learning_rate*sum(weight_d)/len(weight_d)               # Promedia los gradientes y da un paso contra el gradiente (por eso el "-=")
  ##########################################################

  print(f"Weight: {w: .2f}, Cost: {cost:.2f}")                # w ya actualizado; cost es el de antes de actualizar

# --- Prueba ---
test_inputs = [5, 6]
test_targets = [10, 12]
pred = [predict(i) for i in test_inputs]
for i, t, p in zip(test_inputs, test_targets, pred):
  print(f"input:{i}, target:{t}, pred:{p:.4f}")
