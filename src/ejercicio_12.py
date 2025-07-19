#Utilizando un ciclo while, calcula el factorial de un número entero n introducido por el usuario y muestra el resultado.

numero_ingresado = int(input('ingrese un numero: '))

factorial = 1
contador = 1

while contador <= numero_ingresado:
    factorial *= contador
    contador +=1

print(f"El factorial de {numero_ingresado} es: {factorial}")

