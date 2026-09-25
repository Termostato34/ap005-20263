import random  # Importa el módulo 'random' para poder generar números aleatorios
from matplotlib import (
    pyplot as plt,
)  # Importa el submódulo 'pyplot' de matplotlib con el alias 'plt' para trazar gráficos

# Add your code below:
numbers_a = (
    range(1, 13)
)  # Crea una secuencia de números del 1 al 12 (útil para representar meses, por ejemplo)
numbers_b = [
    random.randint(1, 1000) for i in range(12)
]  # Genera una lista de 12 números enteros aleatorios entre 1 y 1000 mediante comprensión de listas
plt.plot(
    numbers_a, numbers_b
)  # Dibuja un gráfico de líneas tomando 'numbers_a' para el eje X y 'numbers_b' para el eje Y
plt.show()  # Abre y muestra la ventana con el gráfico generado en pantalla
