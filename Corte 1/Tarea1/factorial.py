while (
    True
):  # Inicia un bucle infinito para repetir la solicitud hasta que el usuario decida salir (o interrumpir)
    value = int(
        input("Enter a positive integer value: ")
    )  # Solicita un valor por consola y lo convierte directamente a entero (int)
    print("Value: ", value)  # Imprime el valor ingresado por el usuario
    a = isinstance(
        value, int
    )  # Comprueba si 'value' es una instancia de la clase entero (siempre será True tras int())
    if (
        a == True and value > 0
    ):  # Evalúa si 'a' es True y si el número ingresado es estrictamente mayor a 0 (positivo)
        fact = 1  # Inicializa la variable acumuladora del factorial en 1
        for i in range(
            1, value + 1
        ):  # Recorre los números desde 1 hasta el valor ingresado inclusive
            fact = (
                fact * i
            )  # Multiplica el acumulador actual por el número de la iteración (calcula el factorial)
        print(
            f"The factorial of {value} is: ", fact
        )  # Imprime el resultado final del factorial calculado
    else:  # Si el número ingresado no es mayor a 0 (es 0 o negativo)...
        print(
            "Please, enter a positive integer number"
        )  # Muestra un mensaje de advertencia pidiendo un número entero positivo
