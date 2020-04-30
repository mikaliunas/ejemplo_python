
print("Menú de opciones para la lista de números a ingresar:")
print("1: ingresar números")
print("2: ordenar números")
print("3: calcular el máximo")
print("4: calcular el mínimo")
print("5: calcular el promedio")
print("0: para terminar")

lista_numeros = []
#pedimos que se ingrese un numero
opcion_elegida = int(input("Ingrese una opcion: "))
#mientras la opcion no sea 0, 
while opcion_elegida is not 0:
    if opcion_elegida == 1:
        #pido que se vuelva a ingresar un numero
        lista_numeros.append(int(input("Ingrese un numero: ")))
    elif opcion_elegida == 2:
        #ordeno la lista de numeros ingresados
        lista_numeros.sort()
        print(lista_numeros)
    elif opcion_elegida == 3:
        #busco el maximo dato de la lista
        print(max(lista_numeros))
    elif opcion_elegida == 4:
        #busco el minimo dato de la lista
        print(min(lista_numeros))
    elif opcion_elegida == 5:
        #imprimo el promedio de todos los numeros ingresados
        print(sum(lista_numeros)/len(lista_numeros))
    print(lista_numeros)

    opcion_elegida = int(input("Ingrese otra opcion: "))

    #en listas ponemos [:] y genera una copia de esta


