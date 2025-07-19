def ej3():
    '''Con un ciclo for, calcula la suma de todos los enteros del 1 al 100 (inclusive) y muestra el resultado final'''
    suma_res=[i for i in range(1,101)]
    suma = 0
    for n in range(len(suma_res)+1):
        suma +=n
    print(suma)
ej3()