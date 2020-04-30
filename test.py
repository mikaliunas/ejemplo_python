n = input("Ingrese un numero: ")
n = int(n)
cont = 0
for i in range(1,n+1):
    if(n/i)==0:
        cont = cont +1
print (cont)
if(cont==2):
    print("El numero es primo")
else:
    print("El numero no es primo")