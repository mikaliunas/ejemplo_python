
import PySimpleGUI as sg
import json

#Funciones que nos ayudan a la resolucion del ejercicio
def leerArchivoJugadores():
    dic_jugadores = {}
    #Tarea: pensar como manejar expections aca
    with open('jugadores.json', 'r') as archivo:
        datos = json.load(archivo)
    return datos
    
def escribirArchivoJugadores(jugadores):
    with open('jugadores.json', 'w') as archivo:
        json.dump(jugadores,archivo)

def cargarJugador(values):
    jugadores = leerArchivoJugadores()
    #sg.Print(jugadores)

    nombre = str(values['_nombre_']).lower()

    if nombre in jugadores.keys():
        if int(values['_puntaje_']) > int(jugadores[nombre]['puntaje']):
            jugadores[nombre] = {
                'puntaje': int(values['_puntaje_']),
                'nivel': int(values['_nivel_']),
                'tiempo': int(values['_tiempo_'])
            } 
        #for key,value in jugadores[nombre].items():
        #    if jugadores[nombre][key] == valures['_'+key+'_']

    else:
        jugadores[nombre] = {
                'puntaje': int(values['_puntaje_']),
                'nivel': int(values['_nivel_']),
                'tiempo': int(values['_tiempo_'])
            }           


    #jugadores[str(values['_nombre_']).lower()] = {
    #    'puntaje': int(values['_puntaje_']),
    #    'nivel': int(values['_nivel_']),
    #    'tiempo': int(values['_tiempo_'])
    #}



#Definir el layout
layout = [
    [sg.Text("Nombre"),sg.Input(key="nombre")],
    [sg.Text("Puntaje"),sg.Input(key="puntaje")],
    [sg.Text("Nivel"),sg.Input(key="nivel")],
    [sg.Text("Tiempo"),sg.Input(key="tiempo")],
    [sg.Button("cargar"), sg.Exit(key="cargar")]
]

window = sg.Window('Ejercicio 5').Layout(layout).Finalize()

#Loop para capturar los eventos de windows
while True:
    event, values = window.Read()

    sg.Print(event)
    sg.Print(values)

    #window.FindElement()

    if event is None or event == 'Exit':
        break
    elif event == 'cargar':
        if values['_nombre_'] == '' or values['puntaje'] == '' or values['nivel'] == '' or values['tiempo'] == '':
            sg.Popup('Falta completar algun campo')
        else:
            cargarJugador(values)