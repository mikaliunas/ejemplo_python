import random

def selecciono_palabra():
    pal = {1:['gato', 'perro','pato','elefante','lobo'], 2:['rojo','azul','verde','amarillo'], 3:['milanesa','pure','pizza','salchicha']}
    tema = int(input('Elige un tema:\n 1: animales\n 2: colores\n 3: comidas\n '))
    palabra = pal[tema][random.randrange(len(pal[tema]))]
    return palabra

def estructura_ahorcado():
    ahorcado = [' O ', '/|\\','/ \\']
    return ahorcado

def separo_palabra(palabra):
    pal_separada = []
    #for y in palabra:
    pal_separada.append('_')
    return pal_separada

def imprimo_pantalla(palabra):
    print ('- '+len(palabra))

def jugar(palabra, pal_separadas, ahorcado):
    cantidad_letras_adivinadas = 0
    cantidad_partes_cuerpo = 0
    sigue = True
    while sigue:
        letra = input('Ingresa una letra: ').lower()
        if letra in palabra:
            for pos in range(len (palabra)):
                if palabra[pos] == letra:
                    pal_separada[pos] = letra
                    cantidad_letras_adivinadas = cantidad_letras_adivinadas + 1
            pal_imprime = ''
            for y in pal_separada:
                pal_imprime = pal_imprime + y + ' '
            print (pal_imprime)
            if cantidad_letras_adivinadas == len(pal):
                print ('Ganaste')
                sigue = False
        else:
            cantidad_partes_cuerpo = cantidad_partes_cuerpo + 1
            for x in range(cantidad_partes_cuerpo):
                print (ahorcado[x])
            if cantidad_partes_cuerpo == 3:
                print ('Perdiste!. La palabra era:', pal)
                sigue = False
jugar_de_nuevo = 'si'
while jugar_de_nuevo == 'si':
    pal = selecciono_palabra
    ahorcado = estructura_ahorcado
    pal_separada = separo_palabra(pal)
    imprimo_pantalla(pal)
    jugar(pal,pal_separada,ahorcado)
    print('Seguis jugando? (si o no)')
    jugar_de_nuevo = input().lower