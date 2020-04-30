import random

preguntas = [['Buenos Aires limita con Santiago del Estero', 'no'], ['Jujuy limita con Bolivia', 'si'], ['San Juan limita con Misiones', 'no']]

#for i in preguntas:
#    print(preguntas)
#    print("-------------------")
#    print(preguntas[0])
#    print("-------------------")
#    print(preguntas[1])
#    print("-------------------")
#    print(preguntas[2])
#    print("-------------------")

lista = range(len(preguntas))
print(list(lista)) 
puntaje = 0

for i in lista:
    num = random.randrange(0,len(preguntas))
    print(num)
    #print(i,preguntas[i])
    print("Responde: "+ preguntas[num][0])
    respuesta = input("si o no?: ").lower()
    if respuesta == preguntas[num][1]:
        print("correcto!")
        puntaje += 1
    else:
        print("incorrecto :(")
    del preguntas[num]

print("Felicitaciones! has conseguido: " +str(puntaje) +" puntos.")