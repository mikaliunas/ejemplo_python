'''def modifico_lista(x):
        x[0]= "cero"
var_original = [1,20]
modifico_lista(var_original)
print(var_original)'''
def imprimirValores(*args):
    for i in args:
        print(i)
('1'*10)
imprimirValores()
print('2'*10)
imprimirValores(1)
print('3'*10)
imprimirValores(1,2)
print('4'*10)
imprimirValores((1,2))
print('5'*10)
imprimirValores([1,2])
print('fin'*10)