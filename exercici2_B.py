"""
El usuario introduce dos números y la función retornará si es PAR o IMPAR.
"""
def parNoPar():
    numero = int(input("Introduce un número: "))
    if numero%2==0:
        mensaje=("{numero} es PAR".format(numero=numero))
    else:
        mensaje=("{numero} es IMPAR".format(numero=numero))
    return mensaje


print(parNoPar())
