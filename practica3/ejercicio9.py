'''def nombres(*datos):
    imprimo = list(enumerate(datos))
    return imprimo

print(nombres(". Rusito",". Lack",". Tobi",". Nacho"))'''

def funcionA(*args):
    print("-"*10)
    resultado = list(enumerate(args))
    for i,nombre in resultado:
        print(f"{i}. {nombre}")
    print("-"*10)

funcionA("Lack","Blackmight","Zeekx", "RusitoLp")