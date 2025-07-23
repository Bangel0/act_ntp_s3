#Mediante un ciclo while, genera y muestra la secuencia de Fibonacci empezando por 1, 1, 2, 3, 5, … y termina cuando se alcance el primer valor mayor que 1000.


# Primeros dos valores de la secuencia
numero  = 1
numero_2= 1

while numero <= 1000:
    print(numero)
    numero, numero_2 = numero_2, numero + numero_2
