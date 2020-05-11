import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import json

#---------------------------------------------------------

def leerArchivo():
	# Tarea: Pensar como manejar exceptions aca
	try:
		with open('jugadores.json', 'r') as archivo:
			datos = json.load(archivo)
		return datos  
	
	except FileNotFoundError:
		with open('jugadores.json', 'w') as archivo:
			datos={}
			json.dump(datos, archivo)        
		return datos

def escribirArchivo(datos):
	with open('jugadores.json' , 'w') as archivo:
		json.dump(datos,archivo)

def cargoDatos(values):
	datos = leerArchivo()
	nombre = str(values['_nombre_']).lower()
	if nombre not in datos.keys():
		datos[nombre] = {
			'Juegos ' : ""
		}
	
	escribirArchivo(datos)

def modificoJugador(jugador,event):
	jugadores = leerArchivo()
	nombre = str(jugador).lower()
	
	if jugadores[nombre]['Juegos '] == "":
		jugadores[nombre]['Juegos '] = event
	else:
		aux = jugadores[nombre]['Juegos '].split('-')
		if event not in aux:
			jugadores[nombre]['Juegos '] = jugadores[nombre]['Juegos ']+" - "+event

	escribirArchivo(jugadores)

#--------------------------------------------------------
#Interfaz ventana de juegos

def faltaCompletar(values):
    if values['_nombre_'] == '':
        return True
    else:
        return False

def elijoJuego(jugador):
	
	layout = [
		[sg.Button('Ahorcado!'),sg.Button('Ta-Te-Ti!'),sg.Button('Reverse!')],
		[sg.Exit()]
	]

	window = sg.Window('Juegos!').Layout(layout).Finalize()

	while True:
		event, values = window.Read()

		if event is None or event == 'Exit':
			break
		elif event == 'Ahorcado!':
			modificoJugador(jugador,event)
			hangman.main()
			window.Close()
			break
		elif event == 'Ta-Te-Ti!':
			modificoJugador(jugador,event)
			tictactoeModificado.main()
			window.Close()
			break
		elif event == 'Reverse!':
			modificoJugador(jugador,event)
			reversegam.main()
			window.Close()
			break

#--------------------------------------------------------

#P.P		
#Definimos la ventana

layout = [
	[sg.Text("Nickname: ") , sg.Input(key='_nombre_')],
	[sg.Button('Elegir juego: '),sg.Exit()]
]

window = sg.Window('ENTRADA DE DATOS').Layout(layout).Finalize() 

#Defino main
def jugar():
	while True:
		event, values = window.Read()
	
		if event is None or event == 'Exit':      
			break
	
		elif (event == 'Elegir juego: '):
			if faltaCompletar(values):                  
				sg.Popup('Falta completar algun campo')
			else:
				cargoDatos(values)
				window.Close()
				elijoJuego(values['_nombre_'])
				#sigo = str(print(input('Quieres jugar a otra cosa? '))).lower
				#if sigo == 'si':
				#	elijoJuego(values(['_nombre_']))
				#else:
				break

jugar()

'''Estuve intentando hacer que al finalizar el juego, y el jugador no querer jugar al mismo juego 
le pregunte si quiere jugar a otra cosa, pero me surgía un error con el main en el doc 
de pySimpleGUI, linea 196 creo, intente con bolean, sacando el window.Close() por si killear la 
ventana era el problema pero no conseguí hacerlo funcionar, también quisiera saber, o si esto 
lo pregunto en practica, como obtener un dato con una elección con frame layout (quise usarlo para probarlo) 
y no supe como obtener el dato de la eleccion, asi mismo como seleccione una sola opción y no dos o todas. 
Y por último gracias, me divertí haciendo este ejercicio, probando cosas y entendiendo más de ésto!'''