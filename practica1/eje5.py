#Genero la frase
frase = """Si trabajás mucho CON computadoras, 
eventualmente encontrarás que te gustaría automatizar 
alguna tarea. Por ejemplo, podrías desear realizar 
una búsqueda y reemplazo en un gran número DE archivos 
de texto, o renombrar y reorganizar un montón de 
archivos con fotos de una manera compleja. Tal vez 
quieras escribir alguna pequeña base de datos 
personalizada, o una aplicación especializada con 
interfaz gráfica, o UN juego simple."""

#Convertimos la frase a minusculas
frase = frase.replace("\n","").lower().split(" ")
frase_nueva = []
#Imprimimos la lista
print(frase)

#Sacamos las palabras repetidas

for i in frase:
    if i not in frase_nueva:
        frase_nueva.append(i)

#Generamos un espacio para separar cosas
print("---------------------------------")

#organizamos la lista
#sorted(list(frase_nueva))

#Otro metodo


#Imprimimos la nueva lista sin las palabras repetidas
print(frase_nueva)