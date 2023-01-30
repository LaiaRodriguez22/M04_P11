'''
 Una funció on demanarà a l’usuari que inserti 2 números
 i el programa li dirà quin és el més gran i quin el més petit.
 Si son iguals sortirà que son iguals.
'''

def majorNum():
    #DEMANO ELS DOS VALORS.
    num1 = int(input("Inserta el primer numero: "))
    num2 = int(input("Inserta el segon numero: "))

    if (num1>num2):
        missatge = "{a} és major que {b}".format(a=num1, b=num2)
    elif (num2>num1): missatge = "{a} és major que {b}".format(a=num2, b=num1)
    else: missatge = "{a} és igual a {b}".format(a=num2, b=num1)

    return missatge


