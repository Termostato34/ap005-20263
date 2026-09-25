for i in range(
    100, 301
):  # Recorre los números enteros desde 100 hasta 300 (301 es exclusivo)
    if (
        i % 12
    ) != 0:  # Evalúa si 'i' NO es divisible por 12 (es decir, el residuo es diferente de 0)
        continue  # Omite el resto de la iteración actual y salta directamente al siguiente número
    print(
        i
    )  # Imprime el número 'i' únicamente cuando la condición de divisibilidad se cumple
