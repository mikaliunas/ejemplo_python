import PySimpleGUI as sg
import json

'''Registrar los jugadores del Ejercicio 3 de la Práctica 3 en un archivo 
utilizando cualquiera de las librerías dadas en la teoría (Pickle, JSON,CSV). 
Implementar una función denominada modificoDatos, la cual solicita (mediante una interfaz generada con PySimpleGUI) 
los datos de unjugador, si este existe en el archivo, modifica dichos datos en el mismo.
Si no existe el jugador, lo agrega.'''
#----------------------------------------------------------

def escribirArchivo(datos):
    with open('jugadores_eje2.json', 'w') as archivo:
        json.dump(datos,archivo)
    #archivo.close()

def leerArchivo():
    try:
        with open('jugadores_eje2.json', 'r') as archivo:
            datos = json.load(archivo)
        return datos  
    
    except FileNotFoundError:
        with open('jugadores_eje2.json', 'w') as archivo:
            datos={}
            json.dump(datos, archivo)        
        return datos

def faltaCompletar(values):
    if values['_nombre_'] == '' or values['_nivel_'] == '' or values['_punmax_'] == '' or values['_tiempo_'] == '':
        return True
    else:
        return False

def cargarDatos(values):

    jugadores = leerArchivo()

    nombre = str(values['_nombre_']).lower
    jugadores[nombre] = {
        'puntaje': int(values['_punmax_']),
        'nivel': int(values['_nivel_']),
        'tiempo': int(values['_tiempo_'])
    }
    escribirArchivo(jugadores)

#----------------------------------------------------------
def modificar(values):
    jugadores = leerArchivo()
    nombre = str(values['_nombre_']).lower

    if nombre in jugadores.keys():
        jugadores[nombre] ={
            'puntaje': int(values['_punmax_']),
            'nivel': int(values['_nivel_']),
            'tiempo': int(values['_tiempo_'])
        }
    escribirArchivo(jugadores)

def modificoDatos():
    layout = [
    [sg.Text("Nombre") , sg.Input(key='_nombre_')],
    [sg.Text('Nivel') , sg.Input(key='_nivel_')],    
    [sg.Text('PuntajeMAX') , sg.Input(key='_punmax_')],    
    [sg.Text('Tiempo') , sg.Input(key='_tiempo_')],    
    [sg.Button("MODIFICAR") , sg.Exit()]
    ]

    window = sg.Window('MODIFICAR DATOS DE JUGADOR').Layout(layout).Finalize()

    while True:
        event, values = window.Read()
    
        if event is None or event == 'Exit':      
            break

        elif event == 'MODIFICAR':
            modificar(values)
            if faltaCompletar(values):                  
                sg.Popup('Falta completar algun campo')                              
            else:                      
                modificar(values)
    window.Close()
#----------------------------------------------------------
#P.P.
#Defino ventana de interfaz

layout = [
    [sg.Text("Nombre: "),sg.Input(key="_nombre_")],
    [sg.Text("Nivel: "),sg.Input(key="_nivel_")],
    [sg.Text("Puntaje Maximo: "),sg.Input(key="_punmax_")],
    [sg.Text("Tiempo: "),sg.Input(key="_tiempo_")],
    [sg.Button("Añadir jugador"), sg.Exit()]
]

window = sg.Window('Ejercicio 2').Layout(layout).Finalize()

#Lleno la estrutura de datos

while True:
    event, values = window.Read()
    
    if event is None or event == 'Exit':
        break
    
    elif event == 'Añadir jugador':
        if faltaCompletar(values):
            sg.Popup('Falta completar algun campo!')
        else:
            cargarDatos(values)

window.Close()

modificoDatos()