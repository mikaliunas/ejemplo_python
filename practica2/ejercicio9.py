#Utilizo una función que genera números aleatorios 
# en un cierto rango 
import random 
numero_compu = random.randrange(50)+1

#Inicializo la variable que cuenta la cantidad de 
#oportunidades y comienzo con el juego
cont=0 
limite = 10
while cont < 11:        
    #Pido ingresar el número al usuario        
    ingresa_numero= int(input('Ingresa el número que pensó la compu en un rango de 0 a 50. \n'))
    
    #Evalúo si es le número generado por la computadora
    if ingresa_numero == numero_compu:
        print ('Ganaste! y lo hiciste en', cont, 'intentos!')
        #cont= 13
        break
    else:
        print ('No.. ese número no es... Sigue pensando..')
        cont= cont + 1
        print('Te quedan: ' +str(limite-cont) +' intentos.')
    #Consulto si uso todos los intentos.. 
    if cont == 3:
        if numero_compu % 2 == 0:
            print("\nEs un numero par!")
        else:
            print("\nEs un numero impar!")
    if cont == 10:
        print ('\n Perdiste :(\n La compu pensó en el número:', numero_compu)