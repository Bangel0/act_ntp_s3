#Con un ciclo for, solicita al usuario que ingrese un número entero positivo y calcula la suma de sus dígitos, mostrando el resultado final.


numero = input("Ingresa un número entero positivo: ")


if numero.isdigit():
    suma = 0
    for digito in numero:
        suma += int(digito)
    print(f"La suma de los dígitos es: {suma}")
else:
    print("Entrada inválida. Por favor, ingresa solo números enteros positivos.")
