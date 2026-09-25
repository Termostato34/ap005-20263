A = 1  # Asigna el valor inicial 1 a la variable 'A' (en mayúscula)
value = input(
    "Ingrese un valor"
)  # Solicita al usuario ingresar un valor por consola (cadena de texto)
value = int(value)  # Convierte el valor ingresado a un número entero

while (
    a == 1
):  # ¡Error de NameError! Intenta evaluar 'a' (minúscula), pero solo existe 'A' (mayúscula)
    for i in range(
        1, value + 1
    ):  # Genera una secuencia de números desde 1 hasta el valor ingresado ('value')
        conta = (
            0  # Inicializa el contador de divisores en 0 para el número 'i'
        )
        for n in range(
            1, i + 1
        ):  # Genera posibles divisores 'n' desde 1 hasta 'i'
            residue = i % n  # Calcula el residuo de dividir 'i' entre 'n'
            if (
                residue == 0
            ):  # Si el residuo es 0, significa que 'n' es divisor exacto de 'i'
                conta = conta + 1  # Incrementa en 1 el contador de divisores

            # print("i = ", i)  # Comentario: Imprimiría el valor actual de 'i'
            # print("n = ", n)  # Comentario: Imprimiría el valor actual del divisor 'n'
            # print("residue = ", residue)  # Comentario: Imprimiría el residuo obtenido
            # print("conta = ", conta)  # Comentario: Imprimiría el contador de divisores acumulados

    # ¡Error de Identación/Lógica! Los bloques 'if' y 'else' de abajo están fuera del ciclo 'for i',
    # por lo que solo evalúan el estado de 'conta' para el ÚLTIMO número alcanzado por 'i'.
    if conta == 2:  # Evalúa si el último número procesado tuvo exactamente 2 divisores (es primo)
        print(f"{i} es un primo")  # Imprime que el último número es primo
        print("\n")  # Imprime un salto de línea adicional
    else:  # Si tuvo un número de divisores diferente de 2...
        print(f"{i} NOOO es un primo")  # Imprime que el último número no es primo
        print("\n")  # Imprime un salto de línea adicional

    print(
        "Do you want to continue?. Press 1 to do that"
    )  # Muestra en consola la opción para continuar en el programa
    a = input()  # Lee la respuesta ingresada por el usuario
    a = int(a)  # Convierte la respuesta a número entero

    if a != 1:  # Si la respuesta ingresada no es igual a 1...
        break  # Detiene la ejecución del bucle 'while' inmediatamente

    value = input(
        "Ingrese un valor"
    )  # Solicita un nuevo número entero para la siguiente iteración del 'while'
    value = int(value)  # Convierte la entrada del usuario a número entero
