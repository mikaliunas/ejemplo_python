def espacio():
    print("-"*10)
numeros = []
contador = 0
while contador < 30:
    num = input('Ingrese numero: ')
    contador = contador+1
    numeros.append(num)

def funcionA(*numeros):
    print(numeros)
    espacio()
    resultado = sum(numeros)
    return resultado

#print(funcionA(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
print(funcionA(numeros))
espacio()
def funcionB(**datosPersonales):
    for k,v in datosPersonales.items():
        print(k,v)
        espacio()

funcionB(nombre=":aaa",apellido=":sss",sexo=":m",nombre1=":bbb",apellido1=":nnn",sexo1=":f")