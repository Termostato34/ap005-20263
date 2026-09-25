tope_rango = 30  # Define el límite superior del rango a evaluar (exclusivo)
n = 0  # Inicializa el contador del ciclo en 0
primo = True  # Bandera (flag) booleana para asumir inicialmente que 'n' es primo

while n < tope_rango:  # Mantiene el ciclo mientras 'n' sea menor a 30
    for div in range(
        2, n
    ):  # Genera divisores desde 2 hasta n-1 para evaluar si es primo
        if n % div == 0:  # Evalúa si 'n' es divisible exactamente por 'div'
            primo = False  # Marca que 'n' NO es primo si la división es exacta
    if primo:  # Evalúa si la bandera se mantuvo como True
        print(n)  # Imprime 'n' por considerarse primo (nota: incluye 0 y 1)
    else:  # Si la bandera cambió a False...
        primo = True  # Reinicia la bandera a True para la siguiente iteración
    n += 1  # Incrementa el valor de 'n' en 1
    n = 0  # Inicializa el número 'n' a evaluar en 0
primo = True  # Asume por defecto que el número es primo
while n < tope_rango:  # Itera hasta alcanzar el límite fijado
    for div in range(2, n):  # Evalúa posibles divisores entre 2 y n-1
        if n % div == 0:  # Si encuentra un divisor exacto...
            primo = False  # Cambia la bandera a False
            break  # Interrumpe el bucle 'for' de inmediato sin evaluar los demás divisores
    if primo:  # Si no se encontró ningún divisor exacto...
        print(n)  # Imprime el número primo
    else:  # Si se detectó que no era primo...
        primo = True  # Restablece la bandera para el siguiente número
    n += 1  # Avanza al siguiente número del rango
# --- Medición SIN break ---
ciclos_sin_break = 0  # Contador de iteraciones internas sin interrupción
n = 0  # Inicialización del número a evaluar
primo = True  # Estado inicial
while n < tope_rango:  # Bucle principal hasta 30
    for div in range(2, n):  # Bucle interno de divisores
        ciclos_sin_break += 1  # Incrementa el contador por cada evaluación ejecutada
        if n % div == 0:  # Comprueba divisibilidad
            primo = False  # Marca como no primo
    if primo:  # Muestra el número si es primo
        print(n)
    else:  # Si no fue primo...
        primo = True  # Restablece el flag
    n += 1  # Siguiente número

print(
    "Cantidad de ciclos: " + str(ciclos_sin_break)
)  # Muestra el total de iteraciones completas (378)

# --- Medición CON break ---
ciclos_con_break = 0  # Contador de iteraciones internas optimizado
n = 0  # Reinicia el valor inicial a 0
primo = True  # Estado inicial
while n < tope_rango:  # Bucle principal hasta 30
    for div in range(2, n):  # Bucle interno de divisores
        ciclos_con_break += 1  # Incrementa el contador acumulativo
        if n % div == 0:  # Comprueba divisibilidad
            primo = False  # Marca como no primo
            break  # Detiene la búsqueda al primer divisor hallado
    if primo:  # Muestra el número si es primo
        print(n)
    else:  # Si no fue primo...
        primo = True  # Restablece el flag
    n += 1  # Siguiente número

print(
    "Cantidad de ciclos: " + str(ciclos_con_break)
)  # Muestra las iteraciones reducidas (134)
print(
    "Se optimizó a un "
    + str(ciclos_con_break / ciclos_sin_break * 100)
    + "% de ciclos aplicando break"
)  # Imprime la relación porcentual entre ambos procesos (~35.45%)
tope_rango = 100  # Aumenta el alcance del cálculo hasta 100

# --- Medición SIN break ---
ciclos_sin_break = 0  # Acumulador de ciclos para la versión ineficiente
n = 0  # Inicializa el conteo en 0
primo = True  # Estado inicial
while n < tope_rango:  # Recorre el rango extendido
    for div in range(2, n):  # Bucle completo de divisores
        ciclos_sin_break += 1  # Registra la ejecución
        if n % div == 0:  # Comprueba divisibilidad
            primo = False  # Marca como no primo
    if primo:  # Muestra primos hallados
        print(n)
    else:  # Si no fue primo...
        primo = True  # Restablece el flag
    n += 1  # Avanza al siguiente número

print(
    "Cantidad de ciclos: " + str(ciclos_sin_break)
)  # Muestra el total sin break (4753)

# --- Medición CON break ---
ciclos_con_break = 0  # Acumulador de ciclos para la versión eficiente
n = 0  # Reinicia la variable de control
primo = True  # Estado inicial
while n < tope_rango:  # Recorre el rango extendido
    for div in range(2, n):  # Bucle con parada temprana
        ciclos_con_break += 1  # Registra la ejecución
        if n % div == 0:  # Comprueba divisibilidad
            primo = False  # Marca como no primo
            break  # Sale del ciclo for inmediatamente al hallar un divisor
    if primo:  # Muestra primos hallados
        print(n)
    else:  # Si no fue primo...
        primo = True  # Restablece el flag
    n += 1  # Avanza al siguiente número

print(
    "Cantidad de ciclos: " + str(ciclos_con_break)
)  # Muestra el total con break (1132)
print(
    "Se optimizó a un "
    + str(ciclos_con_break / ciclos_sin_break * 100)
    + "% de ciclos aplicando break"
)  # Demuestra mayor impacto porcentual en rangos más grandes (~23.81%)

