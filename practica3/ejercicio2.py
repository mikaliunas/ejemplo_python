frase = '''Si trabajás mucho CON computadoras, eventualmente encontrarás 
que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear 
realizar una búsqueda y reemplazo en un gran número DE archivos de texto, 
o renombrar y reorganizar un montón de archivos con fotos de una manera 
compleja. Tal vez quieras escribir alguna pequeña base de datos 
personalizada, o una aplicación  especializada con interfaz gráfica, 
o UN juego simple.'''
frase = frase.lower().replace(",","").replace(".","").replace("\n","").split(" ")
lista = frase
print(lista)
conjunto = set(lista)
def espacio():
    print('-'*20)
espacio()
print(conjunto)
espacio()
dicc={}
for i in conjunto:
    if len(i) not in dicc.keys():
        dicc[len(i)]=[]
    dicc[len(i)].append(i)
espacio()
print('\n'+str(dicc))