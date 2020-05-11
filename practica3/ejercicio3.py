'cant_jugadores = str(input("Ingrese la cantidad de jugadores: "))'
jugadores={}
info={}
'''cant_jugadores = set(cant_jugadores)
for i in cant_jugadores:
    nombre=input("Ingrese nombre del jugador: ")
    nivel=int(input("Ingrese el nivel alcanzado en el juego: "))
    puntaje_max=int(input("Ingrese el puntaje maximo alcanzado: "))
    tiempo_juego=str(input("Ingrese el tiempo total de juego(redondee en horas): "))
    info = {"Nivel: ": nivel, "Puntaje: ": puntaje_max, "Tiempo total de juego: " : tiempo_juego}
    jugadores = {"Jugador: " : nombre, "Informacion: " : info}'''
def espacio():
    print("-"*20)
def leer(datos):
    nombre = input("Ingrese el nombre del jugador:  ")
    if nombre != "ZZZ":
        datos[nombre]={}
        datos[nombre]["Apellido"] = str(input("Ingrese su apellido:  ")) 
        datos[nombre]["Nivel"] = (int(input("Ingrese el nivel del jugador:  ")))
        datos[nombre]["PuntajeMAX"] = (int(input("Ingrese el puntaje max del jugador:  ")))
        datos[nombre]["Tiempo"] = (str(input("Ingrese tiempo de juego en horas:  "))+ " Horas")
    return nombre
#Lleno la estrutura de datos
'''jugadores={
    'LEAN': {'nivel':3,'puntaje':1000,'tiempo':'2 horas'},
    'LEO':{'nivel':4,'puntaje':1400,'tiempo':'3 horas'},
    'ANA':{'nivel':2,'puntaje':400,'tiempo':'1 horas'}
}'''
nombre = leer(jugadores)
while nombre != "ZZZ":
    nombre = leer(jugadores)
espacio()
#Imprimo todo
for jugador in jugadores.items():
    print(jugador)
espacio()
#Imprimo Nombres
for jugador in jugadores:
    print(jugador)
espacio()
#Imprimo jugador con mayor puntaje
print(max(jugadores.items(), key= lambda punt:punt[1]["PuntajeMAX"] ))
