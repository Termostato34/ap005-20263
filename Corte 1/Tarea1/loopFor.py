import time  # Importa el módulo 'time' para poder usar funciones relacionadas con pausas temporales

cadena = "Python"  # Define la cadena de texto "Python" que será recorrida letra por letra

for (
    letra
) in cadena:  # Inicia un bucle 'for' que toma cada carácter de la cadena individualmente en la variable 'letra'
    if (
        letra == "t"
    ):  # Evalúa si la letra actual evaluada es exactamente igual a 't' minúscula
        continue  # Si la condición se cumple, omite el resto del bloque actual y salta a la siguiente iteración (ignora la 't')
    print(
        letra
    )  # Imprime en consola la letra actual (siempre que no haya sido omitida por el 'continue')
    time.sleep(
        1
    )  # Detiene la ejecución del programa durante exactamente 1 segundo antes de continuar con la siguiente letra
