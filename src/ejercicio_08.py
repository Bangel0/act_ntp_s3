def ej_8():
    '''Usando un ciclo while, calcula y muestra los cuadrados de los números del 1 al 20 (1², 2², …, 20²), cada resultado en una línea.'''
    cuadrados = [i for i in range(1,21)]
    it = iter(cuadrados)
    while True:
        try:
            print(next(it)**2)
        except:
            break
ej_8()
