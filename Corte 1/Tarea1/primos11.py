import time  # Importa el módulo 'time' para medir el tiempo de ejecución del programa
inicio = (
    time.time()
)  # Registra el tiempo exacto en segundos al iniciar la ejecución

for i in range(
    1, 31
):  # Recorre los números enteros 'i' desde 1 hasta 30 inclusive (31 es exclusivo)
    conta = 0  # Inicializa el contador de divisores en 0 para cada número 'i'
    for n in range(
        1, i + 1
    ):  # Recorre los posibles divisores 'n' desde 1 hasta el número actual 'i'
        residue = i % n  # Calcula el residuo de dividir 'i' entre 'n'
        if (
            residue == 0
        ):  # Si el residuo es 0, significa que 'n' es un divisor exacto de 'i'
            conta = (
                conta + 1
            )  # Incrementa el contador de divisores en 1 si la división es exacta
    if (
        conta == 2
    ):  # Evalúa si el número 'i' tiene exactamente 2 divisores (por definición, solo 1 y él mismo)
        print(f"{i} es un primo")  # Imprime en consola que el número 'i' es primo
        print("\n")  # Imprime un salto de línea adicional para separar la salida

fin = (
    time.time()
)  # Registra el tiempo exacto en segundos al finalizar todos los ciclos
print(
    "t = ", (fin - inicio) * 1000
)  # Calcula el tiempo transcurrido (fin - inicio), lo convierte a milisegundos multiplicando por 1000 y lo imprime
