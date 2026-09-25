import time  # Importa el módulo 'time' para medir el tiempo transcurrido
inicio = (
    time.time()
)  # Registra la marca de tiempo exacta al iniciar la ejecución del script

for i in range(
    0, 31
):  # Recorre los números enteros 'i' desde 0 hasta 30 inclusive (31 es exclusivo)
    conta = 0  # Inicializa el contador de divisores en 0 para cada número 'i'
    for n in range(
        1, i + 1
    ):  # Recorre los posibles divisores 'n' desde 1 hasta el número actual 'i'
        residue = i % n  # Calcula el residuo de dividir 'i' entre 'n'
        if (
            residue == 0
        ):  # Si el residuo es 0, 'n' es un divisor exacto de 'i'
            conta = (
                conta + 1
            )  # Incrementa el contador de divisores en 1 si la división es exacta
    if (
        conta == 2
    ):  # Evalúa si el número 'i' tiene exactamente 2 divisores (condición clásica de número primo)
        print(
            f"{i} es un primo"
        )  # Imprime el número 'i' si cumple con ser primo

fin = time.time()  # Registra la marca de tiempo exacta al finalizar el ciclo
print(
    "t = ", (fin - inicio) * 1000
)  # Calcula el tiempo total de ejecución restando inicio de fin, lo convierte a milisegundos (*1000) y lo imprime
