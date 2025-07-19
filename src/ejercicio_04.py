def ejercicio_04():
    '''Utilizando un ciclo while, solicita al usuario que ingrese números. El proceso termina cuando el usuario escriba 0. Al final, muestra la suma total de todos los números ingresados.
'''
    numeros=[]
    sum=0
    ingreso = None
    while(ingreso!=0):
        ingreso=int(input("Ingrese numero"))
        numeros.append(ingreso)
    for n in numeros:
        sum+=n
    print(sum)
ejercicio_04()