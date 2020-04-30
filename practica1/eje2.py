#Armamos la frase

frase = """De Nada sirve el porque, de Nada 
sirve el valor, de nada sirve volver, de nada 
sirve el adios. Seguro de nada sirve, yo me 
pregunte hasta cuando te querré como hasta 
hoy, vos me enseñaste llorando que de nada 
sirve el adios, seguro de nada sirve mi amor."""

# palabra a buscar
busqueda = input("Ingrese una palabra: ")

#Generamos lista de palabras separadas
lis = frase.replace("\n","").replace(",","").split(" ")

print(lis)


# pasamos el string a minusculas
busqueda = busqueda.lower()

# dividimos la frase en minuscilas
palabras_frase = frase.lower().split(" ")

# buscamos la palabra
palabras_busqueda = [s for s in palabras_frase if busqueda in s]

# imprimimos en pantalla, la palabra ingresada y la cantidad de veces que aparece
print(palabras_busqueda, len(palabras_busqueda))