imagenes=['im1','im2','im3']

for i in range(0,len(imagenes)):
    x = int(input("Ingrese la coordenada X de la imagen: "))
    y = int(input("\nIngrese la coordenada Y de la imagen: "))
    while y == x:
        y = int(input("\nCoordenada incorrecta, ingrese otra coordenada Y: "))

    imagenes[i] = imagenes[i] + " " + str(x) + " " + str(y)
    imagenes[i] = imagenes[i].split(" ")
print(imagenes)