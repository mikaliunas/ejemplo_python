from functools import reduce

def operaciones(operador, *numeros, **datosPersonales):
    print(operador)
    print(numeros)
    resultado = 0
    if operador == '+':
        resultado = reduce((lambda a,b: a+b), numeros)
    elif operador == '*':
        resultado = reduce((lambda a,b: a*b), numeros)

    print('resultado', resultado)

    for k,v in datosPersonales.items():
        print(k,v)

lista_numeros = [2,3,4,5,6,7,8]
mis_datos={'nombres':'lean','apellido':'mika','direccion':'74 223'}

operaciones('*',*lista_numeros,**mis_datos)