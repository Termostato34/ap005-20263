A = input(
    "Enter a number: "
)  # Solicita un valor por consola y lo guarda como string en la variable 'A' (mayúscula)
a = int(
    a
)  # Convierte la variable 'A' a un número entero y la reasigna a 'a' (minúscula)
b = input(
    "Enter b number: "
)  # Solicita otro valor por consola y lo guarda como string en 'b'
b = float(
    b
)  # Convierte la cadena 'b' a un número decimal (float) y la reasigna
c = (
    a + b
)  # Suma el entero 'a' con el decimal 'b' (el resultado se convierte automáticamente en float) y lo guarda en 'c'

if (
    a == b
):  # Evalúa si el valor numérico de 'a' es exactamente igual al valor de 'b'
    print("equal")  # Se ejecuta si ambos números coinciden en valor
else:  # Si no son iguales...
    print("Different")  # Se ejecuta si los valores son diferentes

print(
    "Type of a is: ", type(a)
)  # Imprime el tipo de dato actual de la variable 'a' (<class 'int'>)
print(
    "Type of b is: ", type(b)
)  # Imprime el tipo de dato actual de la variable 'b' (<class 'float'>)
print("c = ", c)  # Imprime el resultado total de la suma almacenado en 'c'

if (
    type(a) == type(b)
):  # Compara si el tipo de dato de 'a' es idéntico al tipo de dato de 'b'
    print(
        "a and b are of the same type"
    )  # Se ejecuta si ambas variables comparten el mismo tipo
else:  # Si sus tipos de datos son distintos...
    print(
        "a and b are of different type"
    )  # Se ejecuta si tienen tipos diferentes (como en este caso: int vs float)
