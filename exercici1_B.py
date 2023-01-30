"""
El usuario introducirá dos números y la función retornará si uno es mayor o menor al otro número.
"""
def numeros():
    numero1 = int(input("Introduce el primer números: "))
    numero2 = int(input("introduce otro número: "))

    if(numero1 > numero2):
        mensaje = ("{numero2} es MENOR al {numero1}".format(numero1=numero1,numero2=numero2))
    if(numero1 < numero2):
        mensaje = ("{numero2} es MAYOR al {numero1}".format(numero2=numero2,numero1=numero1))

    return mensaje


