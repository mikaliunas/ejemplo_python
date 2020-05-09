import PySimpleGUI as sg
import json
import time

def escribirArchivo(lista):
    with open('Temperatura.json', 'w') as archivo:
        json.dump(lista,archivo)



archivo = open("Temperatura.json", "w") 
layout =[[sg.Text("ingrese la Temperatura.")],
        [sg.InputText(key="temperatura")],
        [sg.Text("ingrese la Humedad.")],
        [sg.InputText(key="humedad")],
        [sg.Button("Anadir"),sg.Button("Cargar a json"),sg.Exit()]]

lista=[]
window = sg.Window("clima").Layout(layout).Finalize()
ok=True
while ok:
        lis=[]
        event , values= window.Read()
        #sg.Print(event)
        #sg.Print(values)
        if event is None or event == "Exit":
                break
        elif event == "Anadir":
                if (values["temperatura"]=="" or values["humedad"]==""):
                    sg.Popup("Falta algun campo")
                else:
                    datos=str(values["temperatura"]),str(values["humedad"])
                    lis.extend(datos)
                    lista.append(lis)
        elif event== "Cargar a json":
           escribirArchivo(lista)
           archivo.close
           ok=False