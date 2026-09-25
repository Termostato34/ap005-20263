# for i in range (1,21):
#     residual = i%2
#     if residual == 0:
#         print(f'{i} is even')
#     else:
#         #print(f'{i} is odd')
#         print(str(i) + ' is odd')

# for i in range (0,6):
#     result = i**3
#     print(result)

times = input(
    "Enter a number of times: "
)  # Solicita un valor por consola y lo guarda como cadena de texto
times = float(
    times
)  # Convierte la cadena ingresada a un número decimal (float)
times = int(
    times
)  # Convierte el float a un número entero (descartando los decimales)
print(
    type(times)
)  # Imprime el tipo de dato final de la variable 'times' (<class 'int'>)
print(times)  # Imprime el valor entero almacenado en 'times'

if times == 0:  # Evalúa si el número ingresado es estrictamente igual a 0
    print(
        "Don't do anything"
    )  # Si es 0, imprime este mensaje y no ejecuta el ciclo
else:  # Si 'times' es diferente de 0 (asumiendo positivo)...
    for (
        i
    ) in (
        range(1, times + 1)
    ):  # Recorre un bucle desde 1 hasta el valor de 'times' inclusive
        print("i = ", i)  # Imprime el número de iteración actual en cada vuelta
