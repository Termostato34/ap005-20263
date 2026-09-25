for i in range(100, 301):  # Recorre números enteros desde 100 hasta 300 (301 es exclusivo)
    if (
        i % 12
    ) != 0:  # Evalúa si 'i' NO es divisible por 12 (residuo diferente de 0)
        continue  # Salta el resto del código y avanza al siguiente número del ciclo
    print(
        i
    )  # Imprime 'i' únicamente cuando SÍ es divisible por 12 (residuo igual a 0)
