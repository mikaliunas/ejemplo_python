#Armamos menu

print("Menú de operaciones para hacer entre numeros: ")
print("1: ingresar número")
print("+: sumar números")
print("-: restar números")
print("*: multiplicar números")
print("/: dividir números")
print("0 para terminar el programa!")

num1 = int(input("Ingrese un número: "))
while num1 is not 0:
    operacion = input("Ingrese operación a realizar: ")
    if operacion == "+":
        num2 = int(input("Ingrese otro número: "))
        resultado = num1 + num2
        print(resultado)
    elif operacion == "-":
        num2 = int(input("Ingrese otro número: "))
        resultado = num1 - num2
        print(resultado)
    elif operacion == "*":
        num2 = int(input("Ingrese otro número: "))
        resultado = num1 * num2
        print(resultado)
    elif operacion == "/":
        num2 = int(input("Ingrese otro número: "))
        resultado = num1 / num2
        print(resultado)
    print("Vamos devuelta!")
    num1 = int(input("Ingrese otro número: "))