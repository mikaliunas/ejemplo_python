#Armamos la frase

frase = """De Nada sirve el porque, de Nada 
sirve el valor, de nada sirve volver, de nada 
sirve el adios. Seguro de nada sirve, yo me 
pregunte hasta cuando te querré como hasta 
hoy, vos me enseñaste llorando que de nada 
sirve el adios, seguro de nada sirve mi amor."""

#Generamos lista de palabras separadas
lis = frase.replace("\n","").replace(",","").split(" ")

print(lis)

#Imprimir strings
print(" ".join(lis))