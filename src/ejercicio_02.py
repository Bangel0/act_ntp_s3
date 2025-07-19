#Mediante un ciclo while, imprime los números enteros del 10 al 1 en orden descendente, cada número en una línea.
contador_inverso=[10]
i=9
while (len(contador_inverso)!=10):
    contador_inverso.append(i)
    i-=1
print(contador_inverso)