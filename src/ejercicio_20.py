#Utilizando un ciclo while, solicita al usuario que ingrese edades una a una. El proceso termina cuando se introduzca -1. Al final, muestra la edad mayor que se haya ingresado.

edad = 0
mayor = 0

while True:
    edad = int(input("Ingresa una edad (o -1 para finalizar): "))
    if edad == -1:
        break
    if edad < 0:
        print("Edad inválida. Intenta de nuevo.")
        continue
    if edad > mayor:
        mayor = edad

print(f"La edad mayor ingresada fue: {mayor}")
