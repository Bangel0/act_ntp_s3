#Mediante un ciclo while, solicita al usuario que escriba palabras. El proceso termina cuando el usuario escriba la palabra “fin”. Al final, muestra cuántas palabras se leyeron (sin contar “fin”).

contador = 0
palabra = ""

while palabra.lower() != "fin":
    palabra = input("Escribe una palabra (escribe 'fin' para terminar): ")
    if palabra.lower() != "fin":
        contador += 1

print(f"Se ingresaron {contador} palabras.")
