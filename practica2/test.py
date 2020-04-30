import random 
cont=0
while (cont != 10):
    numero_compu = random.randrange(3)
    if numero_compu == 0:
        break
    print(numero_compu)
    cont=cont+1