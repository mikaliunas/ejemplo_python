import random
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def juego(palabras):
	#Pido que el jugador elija un tema
	tema = int(input('Elige un tema:\n 1: animales\n 2: colores\n 3: comidas\n '))
	#Selecciono la palabra a trabajar
	pal = palabras[tema][random.randrange(len(palabras[tema]))]
	return pal


def palabraSeparada(pal):
	pal_separada = []
	for y in pal:
		pal_separada.append('_')
	return pal_separada


def palabraParaMostrar(pal_imprime , pal_separada):
	for y in pal_separada:
		pal_imprime = pal_imprime + y + ' '
	print (pal_imprime)


def gano (sigue, cantidad_letras_adivinadas , pal):
	if cantidad_letras_adivinadas == len(pal):
		print ('Ganaste')
		sigue = False
	return sigue

def perdio (sigue, cantidad_partes_cuerpo):
	if cantidad_partes_cuerpo == 3:
		print ('Perdiste!. La palabra era:', pal)
		sigue = False
	return sigue


def jugar (sigue,cantidad_letras_adivinadas,cantidad_partes_cuerpo):
	while sigue:
		print(jugar.__defaults__)	
		letra = input('Ingresa una letra: ').lower()
		if letra in pal:

			for pos in range(len (pal)):

				if pal[pos] == letra:
					pal_separada[pos] = letra
					cantidad_letras_adivinadas = cantidad_letras_adivinadas + 1

			pal_imprime = ''
			palabraParaMostrar(pal_imprime,pal_separada)
			sigue = gano(sigue, cantidad_letras_adivinadas , pal)

		else:
			
			cantidad_partes_cuerpo = cantidad_partes_cuerpo + 1
			for x in range(cantidad_partes_cuerpo):
				print (ahorcado[x])
			sigue = perdio(sigue, cantidad_partes_cuerpo)
		print(jugar.__defaults__)	

palabras = {1:['gato', 'perro','pato','elefante','lobo'], 2:['rojo','azul','verde','amarillo'], 3:['milanesa','pure','pizza','salchicha']}

ahorcado = [' O ', '/|\\','/ \\']

pal = juego(palabras)

pal_separada = palabraSeparada(pal)

print ('- '*len(pal))

cantidad_letras_adivinadas = 0
cantidad_partes_cuerpo = 0

sigue = True

jugar(sigue,cantidad_letras_adivinadas,cantidad_partes_cuerpo)

print('x'*10)
print(jugar.__defaults__)